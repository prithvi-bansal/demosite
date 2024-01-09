from django.test import TestCase, Client
from django.urls import reverse
from .models import User

# Create your tests here.

class DemoTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_demo_dashboard(self):
        client = Client()
        url = reverse('dashboard')
        client.force_login(self.user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_demo_summary(self):
        client = Client()
        client.force_login(self.user)
        url = reverse('summary')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.user.delete()
