
from django.test import TestCase
from core.models import Client, Program

class ModelTestCase(TestCase):
    def test_create_program(self):
        program = Program.objects.create(name="Malaria")
        self.assertEqual(str(program.name), "Malaria")

    def test_create_client(self):
        client = Client.objects.create(
            name="John Mburu",
            age=26,
            contact="0796878314"
        )
        self.assertEqual(client.name, "John Mburu")
        self.assertEqual(client.age, 26)
        self.assertEqual(client.contact, "0796878314")
