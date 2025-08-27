from django.test import Client, TestCase

class SimpleTests(TestCase):
    def test_homepage(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_historia_da_feijoada(self):
        client = Client()
        response = client.get("/historia-da-feijoada/")
        self.assertEqual(response.status_code, 200)

    def test_feijoada_todos_os_dias(self):
        client = Client()
        response = client.get("/feijoada-todos-os-dias/")
        self.assertEqual(response.status_code, 200)

    def test_sobre(self):
        client = Client()
        response = client.get("/sobre/")
        self.assertEqual(response.status_code, 200)

    def test_contato(self):
        client = Client()
        response = client.get("/contato/")
        self.assertEqual(response.status_code, 200)
