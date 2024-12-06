from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserQuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('username',)
