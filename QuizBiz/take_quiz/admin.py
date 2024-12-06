from django.contrib import admin
from .models import UserQuizAttempt, UserAnswer


@admin.register(UserQuizAttempt)
class UserQuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'attempted_at')
    search_fields = ('user', 'quiz')
    list_filter = ('user', 'quiz', 'score', 'attempted_at')


@admin.register(UserAnswer)
class UserAnswer(admin.ModelAdmin):
    list_display = ('attempt', 'question', 'selected_answer', 'is_correct')
    search_fields = ('attempt', 'question')
    list_filter = ('attempt', 'question')
