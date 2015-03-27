from django import forms
from django.contrib.auth.models import User
from ask_app.models import Question, Answer
from django.core.validators import MaxLengthValidator


class CreateUserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20, error_messages={'required': 'Please input your name!'})
    username = forms.CharField(label='Username', max_length=10, error_messages={'required': 'Choose your username!'})
    email = forms.EmailField(error_messages={'required': 'Enter email!'})
    password = forms.CharField(max_length=20)
    repeat = forms.CharField(max_length=20)

    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()  # individual field's clean methods have already been called
        password = cleaned_data.get("password")
        repeat = cleaned_data.get("repeat")

        if password != repeat:
            raise forms.ValidationError("Passwords must be identical.")
        return cleaned_data

    class Meta:
        model = User


class CreateQuestionForm(forms.Form):
    question_label = forms.CharField(label='Label', max_length=20, validators=[MaxLengthValidator(20)], error_messages={'required': 'Please input label!'})  # напиши ошибку заполнения и не более 20 символов
    question_text = forms.CharField(label='Text', max_length=100, validators=[MaxLengthValidator(100)], error_messages={'required': 'Please input text!'})

    class Meta:
        model = Question


class GetVoteForm(forms.Form):
    vote = forms.CharField()
    answer_id = forms.IntegerField()

    class Meta:
        model = Answer


class CreateAnswerForm(forms.Form):
    ans_text = forms.CharField(max_length=200)
    question_id = forms.IntegerField()

    class Meta:
        model = Answer