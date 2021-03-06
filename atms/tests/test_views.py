from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from atms import views

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>ATM Info</h1>')

    def test_home_page_does_not_contain_incorrect_text(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'error')


class MapPageTests(SimpleTestCase):

    def test_map_page_status_code(self):
        response = self.client.get('/atms/map/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('atms-views-map'))
        self.assertEquals(response.status_code, 200)


