from django.db import models
from quiz.models import Quiz, Question
from django.conf import settings


class UserQuizAttempt(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='attempts')
    score = models.IntegerField(default=0)
    attempted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.score}"


class UserAnswer(models.Model):
    attempt = models.ForeignKey(
        UserQuizAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.attempt.user.username} - {self.question.text[:50]} - {'Correct' if self.is_correct else 'Incorrect'}"
