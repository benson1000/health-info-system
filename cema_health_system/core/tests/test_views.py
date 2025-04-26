from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import Client, Program

User = get_user_model()

class ClientViewTestCase(APITestCase):
    def setUp(self):
        # Create a superuser
        self.admin_user = User.objects.create_superuser(username='benso', password='@Benso7130')

        # Force authentication for the test client
        self.client.force_authenticate(user=self.admin_user)

        # Create Programs
        self.program_malaria = Program.objects.create(name="Malaria")
        self.program_hiv = Program.objects.create(name="HIV")
        self.program_tb = Program.objects.create(name="Tuberculosis")

    def test_register_client(self):
        url = reverse('client-list')  # Adjust to your router's client list URL
        data = {
            "name": "John Mburu",
            "age": 26,
            "contact": "0796878314"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_enroll_client(self):
        client = Client.objects.create(
            name="John Mburu",
            age=26,
            contact="0796878314"
        )
        url = reverse('client-enroll', args=[client.id])  # Adjust the enroll URL
        data = {
            "program_ids": [self.program_malaria.id, self.program_hiv.id, self.program_tb.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_client(self):
        Client.objects.create(name="John Mburu", age=26, contact="0796878314")
        url = reverse('client-search') + "?name=John"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_view_client_profile(self):
        client = Client.objects.create(name="John Mburu", age=26, contact="0796878314")
        url = reverse('client-detail', args=[client.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
