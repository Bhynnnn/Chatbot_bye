from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def chatPage(request):
    return render(request, 'chatPage/chatPage.html')

def login(request):
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'register/register.html')

def grades(request):
    return render(request, 'grades/grades.html')


