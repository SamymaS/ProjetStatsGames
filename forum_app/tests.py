from django.test import TestCase
from django.urls import reverse, resolve
from .views import oauth_authorize, oauth_callback, get_games_from_igdb

class URLTests(TestCase):
    def test_oauth_authorize_url(self):
        url = reverse('oauth_authorize')
        self.assertEqual(resolve(url).func, oauth_authorize)

    def test_oauth_callback_url(self):
        url = reverse('oauth_callback')
        self.assertEqual(resolve(url).func, oauth_callback)

    def test_get_games_from_igdb_url(self):
        url = reverse('get_games_from_igdb')
        self.assertEqual(resolve(url).func, get_games_from_igdb)
