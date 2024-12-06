from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quiz, UserAnswer, UserQuizAttempt
from .forms import QuizAttemptForm
from rapidfuzz import fuzz


@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        form = QuizAttemptForm(request.POST, quiz=quiz)
        if form.is_valid():
            attempt = UserQuizAttempt.objects.create(
                user=request.user,
                quiz=quiz
            )

            for question in quiz.questions.all():
                field_name = f'question_{question.id}'
                user_answer = form.cleaned_data.get(field_name)

                if quiz.question_type == 'short':
                    similarity = fuzz.ratio(user_answer.strip().lower(
                    ), question.correct_answer.strip().lower())
                    is_correct = similarity >= 80
                else:
                    is_correct = user_answer == question.correct_answer

                UserAnswer.objects.create(
                    attempt=attempt,
                    question=question,
                    selected_answer=user_answer,
                    is_correct=is_correct
                )

            correct_answers = attempt.answers.filter(is_correct=True).count()
            total_questions = quiz.questions.count()

            attempt.score = (correct_answers / total_questions) * 100
            attempt.save()

            return redirect('quiz_result', attempt_id=attempt.id)

    else:
        form = QuizAttemptForm(quiz=quiz)

    return render(request, 'take_quiz/take_quiz.html', {'form': form, 'quiz': quiz})


@login_required
def quiz_result(request, attempt_id):
    attempt = get_object_or_404(
        UserQuizAttempt, id=attempt_id, user=request.user)
    user_answers = UserAnswer.objects.filter(attempt=attempt)
    score_percentage = attempt.score
    return render(request, 'take_quiz/quiz_result.html', {'attempt': attempt, 'user_answers': user_answers, 'score_percentage': score_percentage})
