from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /posts/5/
    path('<int:announcement_id>/', views.detail, name='detail'),
    # ex: /posts/5/results/
    path('<int:announcement_id>/results', views.results, name='results'),
    # ex: /posts/5/vote/
    path('<int:announcement_id>/vote/', views.vote, name='vote'),
]