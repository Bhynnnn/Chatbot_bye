from django.contrib import admin
from django.urls import path

import ChatbotApp
from . import views

urlpatterns = [
    path('login/', ChatbotApp.views.login, name='login'),
    path('chatPage/', ChatbotApp.views.chatPage, name='chatPage'),
    path('admin/', views.site.urls),
]
