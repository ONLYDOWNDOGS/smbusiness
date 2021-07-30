from django.http import response
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime

from .models import Announcement

# Database is reset for each test method, don't forget!

class AnnouncementModelTests(TestCase):

    def test_was_published_recently_with_future_announcement(self):
        # was_published_recently() returns False for announcements when 
        # pub_date is in the future.
        time = timezone.now() + datetime.timedelta(days=30)
        future_announcement = Announcement(pub_date=time)
        self.assertIs(future_announcement.was_published_recently(), False)

    def test_was_published_recently_with_old_announcement(self):
        # was_published_recently() returns False for announcements when 
        # pub_date is older than 1 day
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_announcement = Announcement(pub_date=time)
        self.assertIs(old_announcement.was_published_recently(), False)

    def test_was_published_recently_with_recent_accouncement(self):
        # was_published_recently() returns True for announcements when
        # pub_date is within the last day
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_announcement = Announcement(pub_date=time)
        self.assertIs(recent_announcement.was_published_recently(), True)


def create_announcement(announcement_text, days):
    """
    Create an announcement with the given `announcement_text` and published the
    given number of `days` offset to now (negative for announcements published
    in the past, positive for announcementss that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Announcement.objects.create(announcement_text=announcement_text, pub_date=time)


class AnnouncementIndexViewTests(TestCase):
    def test_no_announcements(self):
        # If no announcements exist, an error message is thrown
        response = self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['latest_announcement_list'], [])

    def test_past_announcement(self):
        # Announcements with a pub_date in the past are shown on index page
        announcement = create_announcement(announcement_text="Past Announcement.", days=-30)
        response = self.client.get(reverse('posts:index'))
        self.assertQuerysetEqual(
            response.context['latest_announcement_list'],
            [announcement],
        )

    def test_future_announcement(self):
        # Announcements with pub_date in the future aren't shown on index page
        create_announcement(announcement_text="Future announcement.", days=30)
        response = self.client.get(reverse('posts:index'))
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['latest_announcement_list'], [])

    def test_future_question_and_past_question(self):
        # If future and past announcements exist, only past is displayed
        announcement = create_announcement(announcement_text="Past announcement.", days=-30)
        create_announcement(announcement_text="Future announcement.", days=30)
        response = self.client.get(reverse('posts:index'))
        self.assertQuerysetEqual(
            response.context['latest_announcement_list'],
            [announcement],
        )

    def test_two_past_announcements(self):
        # The announcements page may display multiple announcements
        announcement1 = create_announcement(announcement_text="Past announcement 1.", days=-30)
        announcement2 = create_announcement(announcement_text="Past announcement 2.", days=-20)
        response = self.client.get(reverse('posts:index'))
        self.assertQuerysetEqual(
            response.context['latest_announcement_list'],
            [announcement2, announcement1],
        )


class AnnouncementDetailViewTests(TestCase):
    def test_future_announcement(self):
        # The detail view of an announcement with pub_date in the future throws a 404
        future_announcement = create_announcement(announcement_text="Future announcement.", days=5)
        url = reverse('posts:detail', args=(future_announcement.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_announcement(self):
        # The detail view of an announcement with a pub_date in past displays associated text
        past_announcement = create_announcement(announcement_text="Past Announcement.", days=-5)
        url = reverse('posts:detail', args=(past_announcement.id,))
        response = self.client.get(url)
        self.assertContains(response, past_announcement.announcement_text)