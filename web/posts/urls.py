from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('index/', views.IndexView.as_view(), name='index'),
    # ex: /posts/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /posts/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /posts/5/vote/
    path('<int:announcement_id>/vote/', views.vote, name='vote'),
]