from django.urls import path
from .views import take_quiz, quiz_result


urlpatterns = [
    path('take-quiz/<int:quiz_id>/', take_quiz, name='take_quiz'),
    path('quiz-result/<int:attempt_id>/', quiz_result, name='quiz_result'),
]
