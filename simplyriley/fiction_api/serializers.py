# This file translates models.py into json responses

from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
  class Meta:
      model = Story
      fields = ('id', 'title')