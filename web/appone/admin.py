""" Will this correct the linting error that will not stop
occuring? Yep!"""

from django.contrib import admin
from .models import SpaceFact

admin.site.register(SpaceFact)
