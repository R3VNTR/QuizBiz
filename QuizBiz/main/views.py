from django.shortcuts import render
from quiz.models import Quiz


def index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'main/index.html', {'quizzes': quizzes})


def about(request):
    return render(request, 'main/about.html')
