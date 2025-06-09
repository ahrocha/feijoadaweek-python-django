"""feijoadaweek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, sitemaps
from django.contrib.sitemaps.views import sitemap
from feijoadaweek.sitemaps import PostSitemap
from django.urls import path
from core.views import HomePageView, PostDetailView, SobrePageView, ContatoPageView
from django.conf import settings
from django.conf.urls.static import static
from django.templatetags.static import static as static_tag
from django.views.generic import RedirectView

sitemaps_dict = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('sobre/', SobrePageView.as_view(), name='sobre'),
    path('contato/', ContatoPageView.as_view(), name='contato'),
    path('restaurante/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path("sitemaps.xml", sitemap, {'sitemaps': sitemaps_dict}, name='sitemap'),
    path("favicon.ico", RedirectView.as_view(url=static_tag("favicon.ico"), permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
