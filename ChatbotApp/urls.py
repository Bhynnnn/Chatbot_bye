from django.contrib import admin
from django.urls import path

import ChatbotApp
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('chatPage/', views.chatPage, name='chatPage'),
    path('register/', views.register, name='register'),
    path('grades/', views.grades, name='grades'),
    path('admin/', admin.site.urls),

]
