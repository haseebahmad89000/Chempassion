from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Topic, Subtopic, PastPaper, Question, Solution, StudentProgress

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'order']
    search_fields = ['code', 'name']
    ordering = ['order', 'code']

@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ['topic', 'name', 'order']
    list_filter = ['topic']
    search_fields = ['name']

@admin.register(PastPaper)
class PastPaperAdmin(admin.ModelAdmin):
    list_display = ['code', 'year', 'session', 'variant']
    list_filter = ['year', 'session']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['paper', 'question_number', 'topic', 'question_type', 'marks']
    list_filter = ['question_type', 'topic', 'paper']
    search_fields = ['question_text']

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['question', 'correct_answer']

@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'is_correct', 'attempted_at']
    list_filter = ['is_correct', 'user']