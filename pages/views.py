from django.http import HttpResponse
from django.shortcuts import render

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

def votePageView(request, poll_id):
    context = {}
    return render(request, 'vote.html', context, poll_id)

def resultsPageView(request, poll_id):
    context = {}
    return render(request, 'results.html', context)
