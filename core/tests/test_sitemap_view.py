from django.test import Client, TestCase
from django.conf import settings
from django.contrib.sites.models import Site
from core.models import Post

class SitemapViewTests(TestCase):
    
    def setUp(self):

        Site.objects.update_or_create(
            id=settings.SITE_ID,
            defaults={"domain": "feijoadaweek.com.br", "name": "FeijoadaWeek"},
        )
        self.client = Client()
        self.post = Post.objects.create(
            title="Bar Jobim Moema",
            slug="bar-jobim-moema",
            content="conteúdo de teste...",
        )

    def test_sitemap(self):
        response = self.client.get("/sitemap.xml", secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/xml")
        self.assertContains(response, "<url>", count=6)  # 5 static views + 1 post
        expected_url = "https://feijoadaweek.com.br" + self.post.get_absolute_url()
        self.assertContains(response, f"<loc>{expected_url}</loc>", count=1)
