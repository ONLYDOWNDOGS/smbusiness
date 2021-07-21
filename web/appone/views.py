""" HomePageView is setup more complex so that I can use the database
to spit out some mad spacefacts. """


from django.shortcuts import render
from django.views import generic
from django.template.loader import render_to_string
# render_to_string() loads the template like get_template() then renders the string

from .models import SpaceFact


class HomepageView(generic.ListView):

    """ The previously mentioned more complex view. """

    template_name = 'appone/homepage.html'
    context_object_name = 'latest_spacefact_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return SpaceFact.objects.order_by('-pub_date')[:1]


def contact(request):
    """ The view that holds my contact info. """
    # Use render_to_string() to load the template and render it.
    # First, try just rendering the html page that has the {% extends base.html %}
    return render(request, 'appone/contact.html')


def portfolio(request):
    """ The view that contains the links to my portfolio. """

    return render(request, 'appone/portfolio.html')

def examples(request):
    """The view that holds all the site examples. """

    return render(request, 'appone/examples.html')