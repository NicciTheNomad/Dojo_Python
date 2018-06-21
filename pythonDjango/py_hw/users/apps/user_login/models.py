from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, data):
        errors=[]
        if len(data["fname"]) == 0:
            errors.append("first name can not be empty")
        if len(data["email"]) == 0:
            errors.append("email can not be empty")
        if len(errors) == 0:
            return False,
        else:
            return True, errors        

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    # def __str__(self):
    #     return email.self
