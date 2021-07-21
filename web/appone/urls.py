""" Where to make new url addresses. Duh. Because it's called urls is a
pretty good hint of that."""


from django.urls import path
from sendemail.views import emailview
from . import views


app_name = 'appone'


urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage/'),
    path('contact/', emailview, name='contact/'),
    path('portfolio/', views.portfolio, name='portfolio/'),
    path('examples/', views.examples, name='examples/'),
]
