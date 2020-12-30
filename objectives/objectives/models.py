from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Objectives(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    importance = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ]
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
