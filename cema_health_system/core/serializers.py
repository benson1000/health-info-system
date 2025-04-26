from rest_framework import serializers
from .models import Client, Program

# Serializer for the Program model
class ProgramSerializer(serializers.ModelSerializer):
    """
    Serializer for the Program model.
    Serializes all fields of the Program to be used in API responses.
    """

    class Meta:
        model = Program
        fields = '__all__'


# Serializer for viewing Client information along with enrolled Programs
class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Client model.
    Includes nested serialization of enrolled Programs (read-only).
    """

    programs = ProgramSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


# Serializer for creating a new Client
class ClientCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new Client.
    Only exposes fields required during client registration: name, age, and contact.
    """

    class Meta:
        model = Client
        fields = ['name', 'age', 'contact']
