from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user for authenticated tests
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create some sample books
        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year='2020')
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year='2021')

    def test_list_books(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books(self):
        url = reverse('book_list') + '?author=Author A'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author A')

    def test_search_books(self):
        url = reverse('book_list') + '?search=Book Two'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book Two')

    def test_order_books(self):
        url = reverse('book_list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], '2021')

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_create')
        data = {'title': 'Book Three', 'author': 'Author C', 'publication_year': '2022'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        url = reverse('book_create')
        data = {'title': 'Book Four', 'author': 'Author D', 'publication_year': '2023'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_update', args=[self.book1.id])
        data = {'title': 'Updated Book One', 'author': 'Author A', 'publication_year': '2020'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

