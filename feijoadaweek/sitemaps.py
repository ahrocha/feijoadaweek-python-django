from django.contrib.sitemaps import Sitemap
from core.models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.published_at

    def location(self, obj):
        return f"/restaurante/{obj.slug}"
