from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]

from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
