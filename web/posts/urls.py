from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /posts/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /posts/5/results/
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # ex: /posts/5/vote/
    path('<int:announcement_id>/vote/', views.vote, name='vote'),
]