from django.urls import path, include
from .views import new_post

urlpatterns = [
    path('', new_post, name = 'post'),
]