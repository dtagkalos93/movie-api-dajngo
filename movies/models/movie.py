from django.db import models


class Movie(models.Model):
    image = models.CharField(max_length=128)
    title = models.CharField(max_length=64)
    plot = models.TextField()
    genres = models.CharField(max_length=128)
    duration = models.CharField(max_length=64)
