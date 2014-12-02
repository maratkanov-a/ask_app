from django.contrib import admin

from ask_app.models import Question, User, Answer

admin.site.register(Question)
admin.site.register(Answer)