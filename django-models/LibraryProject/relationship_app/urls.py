from django.urls import path
from .views import register
from .views import register, list_books, LibraryDetailView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book
from django.contrib.auth.views import LoginView, LogoutView


# app_name = 'relationship_app'

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('library/<str:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
