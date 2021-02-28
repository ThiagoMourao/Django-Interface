from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'produto/index.html')

def about(request):
    return render(request, 'produto/about.html')