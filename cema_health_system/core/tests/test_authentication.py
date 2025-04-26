from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class AuthenticationTestCase(APITestCase):
    def test_block_unauthenticated_access(self):
        url = reverse('client-list')  # Adjust to your router
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)