from django.test import TestCase, Client
from lms_app.models import *
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.index_url = reverse('index')
        self.books_url = reverse('books')
        Book.objects.create(title='test', author='test', pages=1, price=1, rental_price_day=1, rental_period=1,
                            status='available', category=Category.objects.create(name='test'))

    def test_get_index(self):
        response = self.c.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_post_index(self):
        response = self.c.post(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_delete_index(self):
        response = self.c.delete(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_put_index(self):
        response = self.c.put(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_get_books(self):
        response = self.c.get(self.books_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/books.html')
