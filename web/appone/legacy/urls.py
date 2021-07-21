from django.urls import path
from . import views


app_name = 'appone'


# Make a pattern for contacts and portfolio!
urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage/'),
    path('contact/', views.ContactView.as_view(), name='contact/'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio/'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
