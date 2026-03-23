from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """IGCSE Chemistry 0620 Topics"""
    code = models.CharField(max_length=10, help_text="e.g., 1.1, 2.3")
    name = models.CharField(max_length=200, help_text="e.g., States of Matter")
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        ordering = ['order', 'code']

class Subtopic(models.Model):
    """Subtopics within main topics"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='subtopics')
    name = models.CharField(max_length=200)
    explanation = models.TextField(blank=True)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube video link")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.topic.code} - {self.name}"
    
    class Meta:
        ordering = ['order']

class PastPaper(models.Model):
    """Past paper reference"""
    SESSION_CHOICES = [
        ('m', 'May/June'),
        ('o', 'October/November'),
        ('f', 'Feb/March'),
    ]
    
    year = models.IntegerField()
    session = models.CharField(max_length=1, choices=SESSION_CHOICES)
    variant = models.IntegerField(help_text="Paper variant: 1, 2, or 3")
    
    question_paper_url = models.URLField(blank=True, null=True)
    mark_scheme_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"0620_s{self.year}_{self.session}_{self.variant}"
    
    @property
    def code(self):
        return f"0620_s{self.year}_{self.session}_{self.variant}"

class Question(models.Model):
    QUESTION_TYPES = [
        ('mcq', 'Multiple Choice'),
        ('structured', 'Structured'),
        ('practical', 'Practical'),
        ('theory', 'Theory'),
    ]
    
    paper = models.ForeignKey(PastPaper, on_delete=models.CASCADE, related_name='questions')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.SET_NULL, null=True, blank=True)
    question_number = models.CharField(max_length=10, help_text="e.g., 1a, 2c")
    question_text = models.TextField()
    marks = models.IntegerField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='mcq')
    image_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.paper.code} - Q{self.question_number}"

class Solution(models.Model):
    """Model for solutions and explanations"""
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='solution')
    correct_answer = models.TextField(help_text="For MCQ: e.g., 'B'. For structured: model answer")
    explanation = models.TextField()
    video_explanation_url = models.URLField(blank=True, null=True)
    common_mistakes = models.TextField(blank=True)
    marking_points = models.JSONField(default=list, help_text="List of marking points")
    examiner_tip = models.TextField(blank=True)
    
    def __str__(self):
        return f"Solution for {self.question}"

class StudentProgress(models.Model):
    """Track student progress on questions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_attempted = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=False)
    answer_given = models.TextField(blank=True)
    time_taken_seconds = models.IntegerField(null=True, blank=True)
    attempted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'question']
    
    def __str__(self):
        return f"{self.user.username} - {self.question} - {'Correct' if self.is_correct else 'Incorrect'}"
class TopicNote(models.Model):
    """Study notes for each topic"""
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField(help_text="Write notes in markdown or HTML format")
    pdf_file = models.FileField(upload_to='notes/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Notes for {self.topic.name}"

class Video(models.Model):
    """Video resources for subtopics"""
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    youtube_url = models.URLField(help_text="YouTube video link")
    duration = models.CharField(max_length=20, blank=True, help_text="e.g., 15:30")
    thumbnail = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.subtopic.name}: {self.title}"
    
    class Meta:
        ordering = ['order']

class LiveClass(models.Model):
    """Live online classes"""
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='live_classes')
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    zoom_link = models.URLField(help_text="Zoom/Google Meet/YouTube Live link")
    recording_url = models.URLField(blank=True, null=True, help_text="Recording link after class")
    is_upcoming = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d %H:%M')}"