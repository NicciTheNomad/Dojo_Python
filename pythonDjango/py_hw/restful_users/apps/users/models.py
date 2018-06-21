from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, data):
        errors = []
        if len(data["first_name"]) == 0:
            errors.append("name can not be empty")
        if len(data["last_name"]) == 0:
            errors.append("email can not be empty")
        if len(data["email"]) == 0:
            errors.append("name can not be empty")        
        if len(errors) == 0:
            return False,
        else:
            return True, errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()              
