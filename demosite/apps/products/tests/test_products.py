from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

# import django
# django.setup()

def test_demo_dashboard():
    client = Client()
    # url = reverse('dashboard')
    response = client.get('/products/dashboard/')
    assert response.status_code == 200


def test_demo_summary():
    client = Client()
    url = reverse('summary')
    response = client.get(url)
    assert response.status_code == 200
