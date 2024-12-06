from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from take_quiz.models import UserQuizAttempt
from quiz.models import Quiz


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('home'))
        else:
            return render(request, 'user/login.html', {'form': form, 'error': 'Invalid credentials'})

    else:
        form = AuthenticationForm()

    return render(request, 'user/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    quiz_attempts = UserQuizAttempt.objects.filter(user=request.user)
    created_quizzes = Quiz.objects.filter(created_by=request.user)
    return render(request, 'user/profile.html', {
        'user': request.user,
        'quiz_attempts': quiz_attempts,
        'created_quizzes': created_quizzes,
    })
