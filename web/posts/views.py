from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm

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


class HomepageView(generic.ListView):

    template_name = 'posts/homepage.html'
    context_object_name = 'latest_announcement_list'

    def get_queryset(self):
        # Excludes announcements that aren't published yet
        return Announcement.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:1]

def emailview(request):
    """ This handles the emails, where they go, etc. """

    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                        ['jonathanecooke90@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'posts/success.html')
    return render(request, 'posts/email.html', {'form': form})
    