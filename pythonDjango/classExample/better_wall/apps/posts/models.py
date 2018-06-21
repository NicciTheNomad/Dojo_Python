from __future__ import unicode_literals
from ..users.models import User
from django.db import models

# Create your models here.
#posts

class Message(models.Model):
    content = models.TextField(null=True, blank=True)
    logged_in = models.ForeignKey(User, related_name="message_left")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(null=True, blank=True)
    message = models.ForeignKey(Message, related_name="comment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

