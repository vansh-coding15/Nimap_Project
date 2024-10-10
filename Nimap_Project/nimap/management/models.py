from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='projects', blank=True)

    def __str__(self):
        return self.name
