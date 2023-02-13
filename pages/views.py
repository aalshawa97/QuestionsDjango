from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def homePageView(request):
    return render(request, 'home.html')


def aboutPageView(request):
    context = {}
    return render(request, 'Templates/about.html', context)


def createPageView(request):
    context = {}
    return render(request, 'poll/create.html', context)


def votePageView(request):
    context = {}
    return render(request, 'poll/vote.html', context)


def resultsPageView(request):
    context = {}
    return render(request, 'poll/results.html', context)
