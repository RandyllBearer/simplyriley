from django.urls import path
from .views import CreateStoryView
from .views import IndexStoryView

urlpatterns = [
  path('create_story', CreateStoryView.as_view()),
  path('index_stories', IndexStoryView.as_view())
]