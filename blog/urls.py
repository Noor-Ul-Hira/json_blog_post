from django.urls import path
from .views import index, create_post, api_posts

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_post, name='create_post'),
    path('api/posts/', api_posts, name='api_posts'),
]