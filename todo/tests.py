from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .models import ListElement

# Create your tests here.


def create_list_element(text):
    text = 'Test'
    return ListElement.objects.create(text=text)


class ListElementCreateViewTests(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def test_no_elements(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listelement_form.html')
        self.assertContains(response, 'No todo elements yet.')
        self.assertQuerysetEqual(response.context['list_elements'], [])

    def test_element_created(self):
        response = self.client.post(reverse('index'))
