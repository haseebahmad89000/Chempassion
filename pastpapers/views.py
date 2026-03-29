from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import json
import os
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from .models import Topic, Subtopic, Question, Video, LiveClass, StudentProgress, TopicNote

def home(request):
    topics = Topic.objects.annotate(
        question_count=Count('question')
    ).order_by('order')
    
    context = {
        'topics': topics,
    }
    return render(request, 'pastpapers/home.html', context)

def topics_list(request):
    topics = Topic.objects.annotate(
        question_count=Count('question')
    ).order_by('order')
    return render(request, 'pastpapers/topics.html', {'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    subtopics = topic.subtopics.all().order_by('order')
    for subtopic in subtopics:
        subtopic.question_count = subtopic.question_set.count()
    
    context = {
        'topic': topic,
        'subtopics': subtopics,
    }
    return render(request, 'pastpapers/topic_detail.html', context)

def topic_practice(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    questions = topic.question_set.select_related('solution').all()
    context = {
        'questions': questions,
        'title': f'Topic {topic.code}: {topic.name}',
        'topic_id': topic_id,
    }
    return render(request, 'pastpapers/practice.html', context)

def subtopic_practice(request, subtopic_id):
    subtopic = get_object_or_404(Subtopic, id=subtopic_id)
    questions = subtopic.question_set.select_related('solution').all()
    context = {
        'questions': questions,
        'title': subtopic.name,
        'topic_id': subtopic.topic.id,
    }
    return render(request, 'pastpapers/practice.html', context)

def revision_notes(request):
    """Display revision notes page"""
    topics = Topic.objects.all().order_by('order')
    notes_dict = {}
    for topic in topics:
        try:
            note = TopicNote.objects.get(topic=topic)
            notes_dict[topic.id] = note.content
        except TopicNote.DoesNotExist:
            notes_dict[topic.id] = f"<h2>📖 Notes for {topic.name}</h2><p>Coming soon! Check back later for detailed revision notes.</p>"
    
    context = {
        'topics': topics,
        'notes': notes_dict,
    }
    return render(request, 'pastpapers/revision_notes.html', context)

def subtopic_detail(request, subtopic_id):
    """Display detailed notes for a specific subtopic"""
    subtopic = get_object_or_404(Subtopic, id=subtopic_id)
    topic = subtopic.topic
    
    try:
        note = TopicNote.objects.get(topic=topic)
        content = note.content
    except TopicNote.DoesNotExist:
        content = f"<h2>Notes for {subtopic.name}</h2><p>Coming soon!</p>"
    
    context = {
        'subtopic': subtopic,
        'topic': topic,
        'content': content,
    }
    return render(request, 'pastpapers/subtopic_detail.html', context)

def get_subtopic_content(request, subtopic_id):
    """API endpoint to get subtopic content and syllabus statements"""
    subtopic = get_object_or_404(Subtopic, id=subtopic_id)
    topic = subtopic.topic
    
    # Load content from JSON file if exists
    content_file = os.path.join(os.path.dirname(__file__), 'subtopic_content.json')
    content_data = {}
    try:
        with open(content_file, 'r') as f:
            content_data = json.load(f)
    except FileNotFoundError:
        pass
    
    # Get statements for this subtopic
    statements = []
    if str(subtopic_id) in content_data:
        statements = content_data[str(subtopic_id)].get('statements', [])
    else:
        # Default statements based on subtopic ID
        statements = [
            {"question": "Understanding this topic", 
             "answer": f"<p>Detailed revision notes for {subtopic.name} will be added soon. Check back later!</p>"}
        ]
    
    # Get full content from TopicNote
    try:
        note = TopicNote.objects.get(topic=topic)
        full_content = note.content
    except TopicNote.DoesNotExist:
        full_content = f"<h2>{subtopic.name}</h2><p>Detailed notes coming soon!</p>"
    
    return JsonResponse({
        'content': full_content,
        'statements': statements,
        'subtopic_name': subtopic.name,
        'topic_name': topic.name
    })

def flashcards(request):
    topics = Topic.objects.all().order_by('order')
    return render(request, 'pastpapers/flashcards.html', {'topics': topics})

def exam_questions(request):
    topics = Topic.objects.all().order_by('order')
    return render(request, 'pastpapers/exam_questions.html', {'topics': topics})

def past_papers(request):
    return render(request, 'pastpapers/past_papers.html')

def mock_exams(request):
    return render(request, 'pastpapers/mock_exams.html')

def target_test(request):
    return render(request, 'pastpapers/target_test.html')

def strengths_weaknesses(request):
    if not request.user.is_authenticated:
        return redirect('login')
    progress = StudentProgress.objects.filter(user=request.user)
    weak_topics = []
    topics = Topic.objects.all()
    for topic in topics:
        topic_progress = progress.filter(question__topic=topic)
        attempted = topic_progress.count()
        if attempted > 0:
            correct = topic_progress.filter(is_correct=True).count()
            weak_topics.append({
                'topic': topic,
                'accuracy': (correct / attempted * 100),
                'attempted': attempted,
                'correct': correct
            })
    return render(request, 'pastpapers/strengths_weaknesses.html', {'weak_topics': weak_topics})

def live_classes(request):
    all_classes = LiveClass.objects.all().order_by('-date')
    upcoming = LiveClass.objects.filter(is_upcoming=True, date__gte=datetime.now()).order_by('date')
    context = {
        'live_classes': all_classes,
        'upcoming': upcoming,
    }
    return render(request, 'pastpapers/live_classes.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'pastpapers/register.html', {'form': form})

@login_required
def dashboard(request):
    progress = StudentProgress.objects.filter(user=request.user)
    total_attempted = progress.count()
    correct_count = progress.filter(is_correct=True).count()
    accuracy = (correct_count / total_attempted * 100) if total_attempted > 0 else 0
    
    weak_topics = []
    topics = Topic.objects.all()
    for topic in topics:
        topic_progress = progress.filter(question__topic=topic)
        attempted = topic_progress.count()
        if attempted > 0:
            correct = topic_progress.filter(is_correct=True).count()
            if (correct / attempted) < 0.5:
                weak_topics.append({
                    'topic': topic,
                    'accuracy': (correct / attempted * 100),
                    'attempted': attempted
                })
    
    context = {
        'total_attempted': total_attempted,
        'correct_count': correct_count,
        'accuracy': round(accuracy, 1),
        'weak_topics': weak_topics,
        'recent_activity': progress.order_by('-attempted_at')[:10],
    }
    return render(request, 'pastpapers/dashboard.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        return redirect('profile')
    return render(request, 'pastpapers/profile.html', {'user': request.user})

@login_required
@csrf_exempt
def save_progress(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_id = data.get('question_id')
        is_correct = data.get('is_correct')
        answer_given = data.get('answer_given')
        
        question = get_object_or_404(Question, id=question_id)
        
        progress, created = StudentProgress.objects.update_or_create(
            user=request.user,
            question=question,
            defaults={
                'is_attempted': True,
                'is_correct': is_correct,
                'answer_given': answer_given,
            }
        )
        
        return JsonResponse({'status': 'saved'})
    return JsonResponse({'error': 'Invalid request'}, status=400)