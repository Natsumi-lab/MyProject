from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.age})"
