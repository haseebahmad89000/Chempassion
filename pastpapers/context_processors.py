from .models import Topic

def topics_processor(request):
    """Add topics to all templates automatically"""
    try:
        topics = Topic.objects.all().order_by('order')
        # Add counts to each topic
        for topic in topics:
            topic.question_count = topic.question_set.count()
            topic.subtopic_count = topic.subtopics.count()
        return {'topics': topics}
    except:
        return {'topics': []}