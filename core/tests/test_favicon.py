from django.test import Client, TestCase
from django.templatetags.static import static


class FaviconViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_has_favicon_link(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        favicon_url = static("favicon.ico")
        self.assertContains(
            response,
            f'<link rel="icon" href="{favicon_url}" type="image/x-icon">'
        )

    def test_favicon_served_correctly(self):
        favicon_url = static("favicon.ico")
        response = self.client.get(favicon_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Type"],
            "image/x-icon",
            f"Content-Type inesperado: {response['Content-Type']}"
        )
