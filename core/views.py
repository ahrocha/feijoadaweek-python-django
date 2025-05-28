from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'core/home.html'
    context_object_name = 'posts'
    ordering = ['-published_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'