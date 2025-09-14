from django.urls import path
from .views import list_books, BookDetailView

app_name = 'bookshelf'

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
