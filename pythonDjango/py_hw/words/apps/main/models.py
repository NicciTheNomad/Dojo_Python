from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Word(models.Model):
    COLOR_CHOICES = (
        ('red', 'red'),
        ('green', 'green'),
        ('blue', 'blue'),
    )
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)
    COLOR_NEXT_CHOICES = (
        ('yellow', 'yellow'),
        ('purple', 'purple'),
        ('black', 'black'),
    )
    color_next = models.CharField(max_length=100, choices=COLOR_NEXT_CHOICES)
    word = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

