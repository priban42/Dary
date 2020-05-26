import uuid

from django.db import models

class Dar(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=300, default="")
    img_url = models.CharField(max_length=500, default="")
    rezervace = models.BooleanField(default=False)