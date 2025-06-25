from django.contrib.sitemaps import Sitemap
from core.models import Post
from django.urls import reverse

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.published_at

    def location(self, obj):
        return f"/restaurante/{obj.slug}/"

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ['home', 'sobre', 'contato', 'historia_da_feijoada']

    def location(self, item):
        return reverse(item)
