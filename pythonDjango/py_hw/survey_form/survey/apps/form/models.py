from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_data(self, data):
        errors = []
        if len(data['fname']) == 0:
            errors.append('name cannot be empty')
        if len(data['lname']) == 0:
            errors.append('name cannot be empty')
        if len(errors) == 0:
            return False,
        else:
            return True, errors        

class User(models.Model):
    LANGUAGE_CHOICES = (
        ('Java', 'Java'),
        ('Ruby', 'Ruby'),
    )
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    LOCATION_CHOICES = (
        ('SanJose', 'SanJose'),
        ('Seattle', 'Seattle'),
    )
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()