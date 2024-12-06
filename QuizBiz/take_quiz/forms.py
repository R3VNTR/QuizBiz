from django import forms
from .models import Quiz, Question, UserAnswer, UserQuizAttempt


class QuizAttemptForm(forms.Form):
    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop('quiz')
        super().__init__(*args, **kwargs)

        for question in quiz.questions.all():
            field_name = f'question_{question.id}'

            if quiz.question_type == 'mcq':
                self.fields[field_name] = forms.ChoiceField(
                    label=question.text,
                    choices=[(option, option) for option in question.options],
                    widget=forms.RadioSelect
                )
            elif quiz.question_type == 'tf':
                self.fields[field_name] = forms.ChoiceField(
                    label=question.text,
                    choices=[('True', 'True'), ('False', 'False')],
                    widget=forms.RadioSelect
                )
            elif quiz.question_type == 'short':
                self.fields[field_name] = forms.CharField(
                    label=question.text,
                    widget=forms.Textarea(attrs={'rows': 2, 'cols': 40})
                )
