from email.mime import image
from os import link
from pydoc import resolve
from turtle import title
from urllib import response
from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
from .models import Episode

class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title="My awesome Podcast episode",
            description = "Look mom, I made it",
            pub_date = timezone.now(),
            link = "https://myawesomeshow.com",
            image="https://image.myawesomeshow.com",
            podcast_name = "My Python Podcast",
            guid = "de194720-7b4c-49e2-a05f-432436d3fetr",
        )
    def test_episode_content(self):
        self.assertEqual(self.episode.description, "Look mom, I made it")
        self.assertEqual(self.episode.link, "https://myawesomeshow.com")
        self.assertEqual(self.episode.guid, "de194720-7b4c-49e2-a05f-432436d3fetr")
    def test_episode_str_representation(self):

        self.assertEqual(str(self.episode), "My Python Podcast: My awesome Podcast episode")
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "homepage.html")

    def test_homepage_list_contains(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "My awesome Podcast episode")
