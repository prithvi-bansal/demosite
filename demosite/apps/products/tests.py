from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

def demo_test_dashboard(self):
    client = Client()
    url = reverse('dashboard')
    response = client.get(url)
    self.assertEqual(response.status_code, 200)


def demo_test_summary(self):
    client = Client()
    url = reverse('summary')
    response = client.get(url)
    self.assertEqual(response.status_code, 200)
