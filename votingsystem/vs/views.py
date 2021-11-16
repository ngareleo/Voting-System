from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':

        # we get the data from the body
        return redirect('/')


def vote(request):
    pass

