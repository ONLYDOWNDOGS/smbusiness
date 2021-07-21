""" The models for the spacefacts. "Loosely" based on the django tutorial
and by loosely i mean very. """


from django.db import models


class SpaceFact(models.Model):

    """ Class to make Spacefacts. To make more, go to manage.py shell and
    after importing this class and timezone from django.utils, run SpaceFact(
    spacefact_text="#", pub_date=timezone.now()) """

    spacefact_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.spacefact_text
