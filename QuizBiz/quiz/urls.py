from django.urls import path
from .views import create_quiz, create_questions, quiz_summary, quiz_details, delete_quiz


urlpatterns = [
    path('create_quiz/', create_quiz, name='create_quiz'),
    path('quiz_summary/', quiz_summary, name='quiz_summary'),
    path('create_quiestions/', create_questions, name='create_questions'),
    path('quiz_details/<int:quiz_id>/', quiz_details, name='quiz_detail'),
    path('delete_quiz/<int:quiz_id>', delete_quiz, name='delete_quiz')
]
