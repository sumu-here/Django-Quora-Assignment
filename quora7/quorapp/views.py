from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import Answers_form,Question_form
from .models import Question,Answers
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

@login_required(login_url="login/")
def index(request):
    all_questions = Question.objects.all().order_by('-created_at')
    return render(request, 'index.html', { 'all_questions': all_questions })

def base(request):
    return render(request,'base.html')

@login_required(login_url="/login/")
def addquestion(request):
    form = Question_form()
    if request.method == 'POST':
        form = Question_form(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)  # Create the question instance but don't save it yet
            question.author = request.user  # Assign the current logged-in user as the author
            question.save()  # Save the question with the author assigned
            return redirect('quorapp:index')
    else:
        all_questions = Question.objects.all().order_by('created_at')
        return render(request, 'addquestion.html', {'form': form, 'all_questions': all_questions})



@login_required(login_url="/login/")
def display_questions(request):
    all_questions = Question.objects.all().order_by('created_at')
    return render(request, 'index.html', {'all_questions': all_questions})

@login_required(login_url="login/")
def detail(request, id):
    question = Question.objects.get(pk=id)
    answers = Answers.objects.filter(question=question).order_by('-updated_at')
    answer_form = Answers_form()

    if request.method == 'POST':
        answer_data = Answers_form(request.POST)
        if answer_data.is_valid():
            answer = answer_data.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('quorapp:detail', id=id)

    return render(request, 'detail.html', {
        'question': question,
        'answers': answers,
        'answer_form': answer_form,
    })



def like_question(request, id):
    question = Question.objects.get(pk=id)
    question.likes += 1
    question.save()

    return redirect('quorapp:index')


def dislike_question(request, id):
    question = Question.objects.get(pk=id)
    question.dislikes += 1
    question.save()

    return redirect('quorapp:index')