from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    color = models.CharField(max_length=50)
    default_status = models.BooleanField()

class Icon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(Application, on_delete=models.CASCADE)
    default_status = models.BooleanField()
