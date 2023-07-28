from django.urls import reverse
from django.db import models


class Url(models.Model):
    real_url = models.CharField(max_length=100)
    shorturl = models.CharField(max_length=100)
