""" Two views, one cup. But yeah these handle the emails to me. """

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


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
            return render(request, 'success.html')
    return render(request, "email.html", {'form': form})


# def successview(request):
# Leads to the success view
#    return render(request, 'success.html')
