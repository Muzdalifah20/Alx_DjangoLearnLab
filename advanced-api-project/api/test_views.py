from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create two authors to use in books
        self.author_a = Author.objects.create(name='Author A')
        self.author_b = Author.objects.create(name='Author B')

        # Create two books linked to the authors
        self.book1 = Book.objects.create(title='Book One', author=self.author_a, publication_year='2020')
        self.book2 = Book.objects.create(title='Book Two', author=self.author_b, publication_year='2021')

    def test_list_books(self):
        """Test listing all books (public access)"""
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        """Test creating a book with authenticated user"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_create')
        data = {
            'title': 'Book Three',
            'author': self.author_a.id,  # author ID must be sent
            'publication_year': '2022',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        """Test updating a book with authenticated user"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_update', args=[self.book1.id])
        data = {
            'title': 'Updated Book One',
            'author': self.author_a.id,
            'publication_year': '2020',
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    def test_delete_book(self):
        """Test deleting a book with authenticated user"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
