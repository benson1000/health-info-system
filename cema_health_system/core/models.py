from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=100)
    programs = models.ManyToManyField(Program, related_name='clients', blank=True)
    
    class Meta:
        ordering = ['name']  # default ordering when you query Clients

    def __str__(self):
        return self.name
