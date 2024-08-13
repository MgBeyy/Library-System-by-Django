from django.test import SimpleTestCase
from django.urls import reverse, resolve

from lms_app import views


class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_books_url_resolves(self):
        url = reverse('books')
        self.assertEqual(resolve(url).func, views.books)

    def test_update_url_resolves(self):
        url = reverse('update', args=[1])
        self.assertEqual(resolve(url).func, views.update)

    def test_delete_url_resolves(self):
        url = reverse('delete', args=[1])
        self.assertEqual(resolve(url).func, views.delete)
