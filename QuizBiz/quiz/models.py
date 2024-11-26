from django.db import models
from django.conf import settings


class Quiz(models.Model):
    TYPE_CHOICES = [
        ('mcq', 'Multiple Choice'),
        ('tf', 'True/False'),
        ('short', 'Short Answer'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(
        max_length=200, help_text="Enter a valid URL for AI to generate questions.", blank=True, null=True)
    num_questions = models.PositiveIntegerField()
    is_public = models.BooleanField(default=True)
    question_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    ai_response = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    options = models.JSONField(null=True, blank=True)
    correct_answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.text
