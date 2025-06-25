from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, TemplateView
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

class SobrePageView(TemplateView):
    template_name = 'core/sobre.html'
    context_object_name = 'sobre'

class ContatoPageView(TemplateView):
    template_name = 'core/contato.html'
    context_object_name = 'contato'

class HistoriaPageView(TemplateView):
    template_name = "core/historia_da_feijoada.html"
