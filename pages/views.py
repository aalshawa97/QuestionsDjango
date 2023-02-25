from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages

from django_project.models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def homePageView(request):
    context = {}
    return render(request, 'home.html', context)

def aboutPageView(request):
    context = {}
    return render(request, 'about.html', context)

def createPageView(request):
    context = {}
    return render(request, 'create.html', context)


def create_question(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']
        if question_text:
            question = Question.objects.create(question_text=question_text)
            messages.success(request, 'Question created successfully.')
            return redirect('question_detail', question_id=question.id)
        else:
            messages.error(request, 'Question text is required.')
    return render(request, 'create_question.html')


def votePageView(request, poll_id):
    context = {}
    return render(request, 'vote.html', context, poll_id)

def resultsPageView(request, poll_id):
    context = {}
    return render(request, 'results.html', context)
