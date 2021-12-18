from django.shortcuts import render
from rest_framework import generics
from .serializers import StorySerializer
from .models import Story

# Create your views here.

# TODO
class CreateStoryView(generics.CreateAPIView):
  queryset = Story.objects.all()
  serializer_class = StorySerializer

# TODO
class IndexStoryView(generics.ListAPIView):
  queryset = Story.objects.all()
  serializer_class = StorySerializer
  