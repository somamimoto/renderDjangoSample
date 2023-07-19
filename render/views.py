from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>This is Render Home.</h1>')
