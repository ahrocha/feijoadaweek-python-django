from django.test import Client, TestCase
from django.templatetags.static import static


class FaviconViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_has_google_analytics(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "G-ZV52Z98X0H")
        self.assertContains(response, "gtag")
