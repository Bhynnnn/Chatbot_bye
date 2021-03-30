from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def chatPage(request):
    return render(request, 'chatPage/chatPage.html')

def login(request):
    return render(request, 'login/login.html')
