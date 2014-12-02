from django.shortcuts import HttpResponse, render, HttpResponseRedirect, render_to_response
from ask_app.models import User, Question, Answer
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from ask_app.forms import CreateUserForm, CreateQuestionForm, GetVoteForm, CreateAnswerForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    questions = Question.objects.order_by('-create_date')

    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    if request.method == 'POST' and request.is_ajax():
        form = CreateAnswerForm(request.POST)
        old_question = Question(id=form.data['question_id'])
        user = User.objects.get(username=request.user.username)
        new_answer = Answer(which_question=old_question, answer_text=form.data['ans_text'], create_date=datetime.now(), ans_author=user)
        new_answer.save()

    for contact in contacts:
        contact.answers = Answer.objects.filter(which_question=contact)
    return render(request, 'home.html', {'questions': questions, 'contacts': contacts})


def home_rating(request):
    if request.method == 'POST' and request.is_ajax():
        answer = Answer.objects.get(id=request.POST['ans_id'])
        answer.rating += int(request.POST['rate'])
        answer.save()
    return HttpResponse()


def registration(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
            new_user.first_name = form.data['first_name']
            new_user.save()
            new_user = authenticate(username=form.data['username'], password=form.data['password'])
            login(request, new_user)
            return HttpResponseRedirect("/home/")
    else:
        form = CreateUserForm()
    return render(request, "registration/registration.html", {'form': form})


@login_required
def userpage(request):
    questions = Question.objects.filter(text_author=request.user)
    answers = Answer.objects.filter(ans_author=request.user)
    return render(request, 'user.html', {'questions': questions, 'answers': answers})


@login_required
def create_question(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                user = User.objects.get(username=request.user.username)
                new_question = Question(label=form.data['question_label'], text=form.data['question_text'], text_author=user, create_date=datetime.now())
                new_question.save()
    else:
        form = CreateQuestionForm()
    return render(request, 'create_question.html', {'form': form})


def search(request):
    if request.method == 'GET':
        questions = Question.objects.filter(label__regex=request.GET['text'])
        return render(request, 'user_questions.html', {'questions': questions})
    return HttpResponse()


