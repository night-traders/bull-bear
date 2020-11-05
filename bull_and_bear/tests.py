from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Stock_ID, Saved_Predictions


class BullAndBearTest(TestCase):

    def test_homepage_status(self):
        self.helper_status_tests('home')
    

    def test_aboutpage_status(self):
        self.helper_status_tests('about')


    def helper_status_tests(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    
    def test_homepage_template(self):
        self.helper_templates_tests('home', 'bull_and_bear/home.html')


    def test_aboutpage_template(self):
        self.helper_templates_tests('about', 'bull_and_bear/about.html')


    def helper_templates_tests(self, url_name, template_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)