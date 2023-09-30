from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    body = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)


