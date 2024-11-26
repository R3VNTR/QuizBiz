from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuizForm
from .models import Quiz, Question
from django.conf import settings
import google.generativeai as genai
import json
from django.contrib import messages

genai.configure(api_key=settings.API_KEY)


@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            url = request.POST.get('url')
            qtype = request.POST.get('question_type')
            num_of_q = request.POST.get('num_questions')

            try:
                generate_mcqs_from_content(url, quiz, qtype, num_of_q)
                messages.success(
                    request, "Quiz created and questions generated successfully!")
                return redirect('home')
            except Exception as e:
                print(f"Error generating MCQs: {e}")
                messages.error(
                    request, "An error occurred while generating questions. Please try again.")
                quiz.delete()

    else:
        form = QuizForm()
    return render(request, 'quiz/create_quiz.html', {'form': form})


@login_required
def quiz_summary(requests):
    pass


@login_required
def create_questions(requests):
    pass


@login_required
def quiz_details(requests, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(requests, 'quiz/quiz_details.html', {'quiz': quiz, 'questions': questions})


@login_required
def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    return redirect('home')


def generate_mcqs_from_content(url, quiz, qtype, num_questions):
    model = genai.GenerativeModel("gemini-1.5-flash")

    if qtype == 'mcq':
        prompt = f"""
                Generate {num_questions} multiple-choice questions based on the content of the URL provided below, with each question having 4 options.
                Ensure that the correct answer is identified in the JSON response.

                URL:
                {url}
                """
    elif qtype == 'tf':
        prompt = f"""
                Generate {num_questions} true/false questions based on the content of the URL provided below.
                Ensure that the correct answer is identified in the JSON response.

                URL:
                {url}
                """
    elif qtype == 'short':
        prompt = f"""
                Generate {num_questions} Short Answer questions based on the content of the URL provided below.
                Ensure that the correct answer is identified in the JSON response.

                URL:
                {url}
                """

    response = model.generate_content(prompt)

    json_formatted = {}

    if response and hasattr(response, 'candidates') and response.candidates:
        generated_text = response.candidates[0].content.parts[0].text.strip()
        json_formatted = json.loads(generated_text.replace(
            '```json\n', '').replace('\n```', ''))
        quiz.ai_response = json_formatted
        quiz.url = url
        quiz.save()

    if qtype == 'mcq':
        for question in json_formatted["questions"]:
            question_txt = question["question"]
            options = question["options"]
            answer = question["answer"]

            question_obj = Question.objects.create(
                quiz=quiz,
                text=question_txt,
                options=options,
                correct_answer=answer
            )

    if qtype == 'tf' or qtype == 'short':
        for question in json_formatted["questions"]:
            question_txt = question["question"]
            answer = question["answer"]

            question_obj = Question.objects.create(
                quiz=quiz,
                text=question_txt,
                correct_answer=answer
            )
