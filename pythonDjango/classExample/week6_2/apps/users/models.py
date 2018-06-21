from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validateData(self, data):
        errors = []
        if len(data["name"]) == 0:
            errors.append("name cannot be empty")
        if len(data["email"]) == 0:
            errors.append("email cannot be empty")  
        if len(errors) == 0:
            return False,
        else:
            return True, errors        

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="blogs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)      

class Admin(models.Model):
    blog = models.ForeignKey(Blog, related_name="admins")
    user = models.ForeignKey(User, related_name="admins_blogs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)