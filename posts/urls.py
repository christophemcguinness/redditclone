from django.urls import re_path
from . import views

app_name = 'posts'

urlpatterns = [
    re_path(r'^create/', views.create, name='create'),
    re_path(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    re_path(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),

]