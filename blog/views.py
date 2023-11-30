# blog/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BlogPostForm
from .models import BlogPost

def index(request):
    # Display a list of blog posts
    posts = BlogPost.get_all_posts()
    return render(request, 'blog/index.html', {'posts': posts})

def create_post(request):
    # Create a new blog post
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_post.html', {'form': form})
def api_posts(request):
    # Return all blog posts in JSON format
    posts = BlogPost.get_all_posts()
    return JsonResponse({'posts': posts})

