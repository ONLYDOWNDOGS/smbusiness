import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


# Linking Announcements to Posts:
# a = Announcement.objects.get(pk=1)
# a.blogpost_set.create(posts_test="Text Here", votes=0)
# a.blogpost_set.create(posts_test="Text Here", votes=0).title  --<to confirm connection>

# This should all be tweaked, just following a "polls" tutorial to refresh db memory
class Announcement(models.Model):
    announcement_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.announcement_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class BlogPost(models.Model):
    title = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    posts_text = models.CharField(max_length=500)
    #added for sake of tutorial and learning, don't think I'll need votes lol
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.posts_text