from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Announcement, BlogPost

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_announcement_list'

    def get_queryset(self):
        # Return the last 5 announcements made
        return Announcement.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    model = Announcement
    template_name = 'posts/detail.html'
    def get_queryset(self):
        # Excludes announcements that aren't published yet
        return Announcement.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Announcement
    template_name = 'posts/results.html'

def vote(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)
    try:
        selected_blogpost = announcement.blogpost_set.get(pk=request.POST['blogpost'])
    except (KeyError, BlogPost.DoesNotExist):
        return render(request, 'posts/detail.html', {
            'announcement': announcement,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_blogpost.votes += 1
        selected_blogpost.save()
        return HttpResponseRedirect(reverse('posts:results', args=(announcement.id)))
