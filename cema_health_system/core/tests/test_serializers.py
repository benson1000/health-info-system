from django.test import TestCase
from core.serializers import ClientSerializer, ProgramSerializer

class SerializerTestCase(TestCase):
    def test_client_serializer_valid(self):
        data = {
            "name": "John Mburu",
            "age": 26,
            "contact": "0796878314"
        }
        serializer = ClientSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_program_serializer_valid(self):
        data = {
            "name": "Malaria"
        }
        serializer = ProgramSerializer(data=data)
        self.assertTrue(serializer.is_valid())