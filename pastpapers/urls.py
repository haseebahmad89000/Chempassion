from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.topics_list, name='topics'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('topic/<int:topic_id>/practice/', views.topic_practice, name='topic_practice'),
    path('subtopic/<int:subtopic_id>/', views.subtopic_detail, name='subtopic_detail'),
    path('subtopic/<int:subtopic_id>/practice/', views.subtopic_practice, name='subtopic_practice'),
    
    # API endpoint for three-column layout
    path('api/subtopic-content/<int:subtopic_id>/', views.get_subtopic_content, name='api_subtopic_content'),
    
    # Revision and Study
    path('revision-notes/', views.revision_notes, name='revision_notes'),
    path('flashcards/', views.flashcards, name='flashcards'),
    path('exam-questions/', views.exam_questions, name='exam_questions'),
    path('past-papers/', views.past_papers, name='past_papers'),
    path('mock-exams/', views.mock_exams, name='mock_exams'),
    path('target-test/', views.target_test, name='target_test'),
    path('strengths-weaknesses/', views.strengths_weaknesses, name='strengths_weaknesses'),
    path('live-classes/', views.live_classes, name='live_classes'),
    
    # User authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='pastpapers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('save-progress/', views.save_progress, name='save_progress'),
]