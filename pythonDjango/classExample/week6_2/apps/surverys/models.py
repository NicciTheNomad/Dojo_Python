from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SurveyManager(models.Manager):
    def validateData(self, data):
        errors = []
        if len(data["survey"]) == 0:
            errors.append("enter survey topic")
        if len(errors) == 0:
            return False,
        else:
            return True, errors        

class Survey(models.Model):
    survey = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = SurveyManager()     

    