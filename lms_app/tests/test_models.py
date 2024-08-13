from unittest import TestCase

from lms_app.models import Book


class TestBook(TestCase):
    def setup(self):
        self.book = Book()

    def test_str(self):
        self.book.title = 'Test Book'
        self.assertEqual(str(self.book), 'Test Book')

    def test_title_and_author(self):
        self.book.title = 'Test Book'
        self.assertEqual(self.book.title_and_author, 'Test Book')

        self.book.author = 'Test Author'
        self.assertEqual(self.book.title_and_author, 'Test Book by Test Author')

        self.book.author = None
        self.assertEqual(self.book.title_and_author, 'Test Book')

        self.book.author = ''
        self.assertEqual(self.book.title_and_author, 'Test Book')
