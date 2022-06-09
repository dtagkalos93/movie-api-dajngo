from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="review")
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(null=True)
