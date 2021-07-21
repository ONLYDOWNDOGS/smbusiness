""" The URL router for the email app. """

from django.contrib import admin
from django.urls import path

from . import views

app_name = 'sendemail'

urlpatterns = [
    path('email/', views.emailview, name='email'),
    # path('success/', views.successview, name='success'),
]
