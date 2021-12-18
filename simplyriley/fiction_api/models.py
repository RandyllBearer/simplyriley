from django.db import models

# Create your models here.

# TODO
class Story(models.Model):
  title = models.CharField(max_length = 128, default="", unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  # for future reference https://docs.djangoproject.com/en/4.0/ref/models/fields/
