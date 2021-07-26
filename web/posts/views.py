from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Announcement

def index(request):
    latest_announcement_list = Announcement.objects.order_by('-pub_date')[:5]
    context = {'latest_announcement_list': latest_announcement_list}
    return render(request, 'posts/index.html', context)

def detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)
    return render(request, 'posts/detail.html', {'announcement': announcement})

def results(request, announcement_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % announcement_id)

def vote(request, announcement_id):
    return HttpResponse("You're voting on nothing lol heres a number %s." % announcement_id)
