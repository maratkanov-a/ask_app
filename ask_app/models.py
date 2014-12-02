from django.db import models
from django.contrib.auth.models import User
import json


class Question(models.Model):
    label = models.CharField(max_length=20, default='Первый вопрос')
    text = models.CharField(max_length=200)
    text_author = models.ForeignKey(User)
    create_date = models.DateTimeField('Дата вопроса')
    # tags = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Answer(models.Model):
    which_question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=200)
    create_date = models.DateTimeField('Дата ответа')
    flag_of_true = models.BooleanField(default=False)
    ans_author = models.ForeignKey(User)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text


