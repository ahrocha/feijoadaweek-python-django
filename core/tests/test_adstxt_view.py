from django.test import Client, TestCase

class AdsTxtViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_ads_txt(self):
        response = self.client.get("/ads.txt", secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "text/plain; charset=utf-8")
        self.assertContains(response, "google.com", count=1)
        self.assertContains(response, "pub-0800147848250371", count=1)
