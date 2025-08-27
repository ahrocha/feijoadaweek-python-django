import datetime
from django.test import Client, TestCase

from core.models import Post

# urlpatterns = [
#     path('', HomePageView.as_view(), name='home'),
#     path('sobre/', SobrePageView.as_view(), name='sobre'),
#     path('historia-da-feijoada/', HistoriaPageView.as_view(), name='historia_da_feijoada'),
#     path('feijoada-todos-os-dias/', FeijoadaTodosOsDiasPageView.as_view(), name='feijoada_todos_os_dias'),
#     path('contato/', ContatoPageView.as_view(), name='contato'),
#     path('restaurante/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
#     path("sitemap.xml", sitemap, {'sitemaps': sitemaps_dict}, name='sitemap'),
#     path("favicon.ico", RedirectView.as_view(url=static_tag("favicon.ico"), permanent=True)),
#     path("ads.txt", adstxt, name="ads-txt"),
# ]

class ViewTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title="Bar Jobim Moema",
            slug="bar-jobim-moema",
            content="conteúdo de teste...",
        )

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")
        self.assertEqual(response.headers["Content-Type"], "text/html; charset=utf-8")

        current_year = datetime.datetime.now().year
        self.assertContains(response, f"{current_year} Feijoada Week")

    def test_sobre(self):
        response = self.client.get("/sobre/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/sobre.html")
        self.assertEqual(response.headers["Content-Type"], "text/html; charset=utf-8")

        current_year = datetime.datetime.now().year
        self.assertContains(response, f"{current_year} Feijoada Week")

        self.assertContains(response, '<h1 class="text-3xl font-bold mb-4">Sobre o Projeto</h1>', html=True)

    def test_historia_da_feijoada(self):
        response = self.client.get("/historia-da-feijoada/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/historia_da_feijoada.html")
        self.assertEqual(response.headers["Content-Type"], "text/html; charset=utf-8")

        current_year = datetime.datetime.now().year
        self.assertContains(response, f"{current_year} Feijoada Week")

        self.assertContains(response, "<h1>A verdadeira história da feijoada</h1>", html=True)

    def test_feijoada_todos_os_dias(self):
        response = self.client.get("/feijoada-todos-os-dias/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/feijoada_todos_os_dias.html")
        self.assertEqual(response.headers["Content-Type"], "text/html; charset=utf-8")

        current_year = datetime.datetime.now().year
        self.assertContains(response, f"{current_year} Feijoada Week")

        self.assertContains(response, "<h1>Onde comer feijoada todos os dias em São Paulo</h1>", html=True)

    def test_contato(self):
        response = self.client.get("/contato/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/contato.html")
        self.assertEqual(response.headers["Content-Type"], "text/html; charset=utf-8")

        current_year = datetime.datetime.now().year
        self.assertContains(response, f"{current_year} Feijoada Week")

        self.assertContains(response, '<h1 class="text-3xl font-bold mb-6">Contato</h1>', html=True)

    def test_post_detail(self):
        response = self.client.get("/restaurante/bar-jobim-moema/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/post_detail.html")
        self.assertEqual(response.headers["Content-Type"], "text/html; charset=utf-8")

        current_year = datetime.datetime.now().year
        self.assertContains(response, f"{current_year} Feijoada Week")

        self.assertContains(response, '<h1 class="text-4xl md:text-5xl font-bold leading-tight text-gray-900 mb-4">Bar Jobim Moema</h1>', html=True)
