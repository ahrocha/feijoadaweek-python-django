from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, TemplateView
from .models import Post, Local

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

class PoliticaDePrivacidadePageView(TemplateView):
    template_name = "core/politica_de_privacidade.html"

class TermosDeUsoPageView(TemplateView):
    template_name = "core/termos_de_uso.html"

# core/feijoada_todos_os_dias
class FeijoadaTodosOsDiasPageView(TemplateView):
    template_name = "core/feijoada_todos_os_dias.html"

class MapaDasFeijoadasPageView(ListView):
    model = Local
    template_name = "core/mapa_das_feijoadas.html"
    context_object_name = 'locais'
    ordering = ['-published_at']

class MapaDasFeijoadasDetailView(DetailView):
    model = Local
    template_name = 'core/local_detail.html'
    context_object_name = 'local'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
