from django.urls import path
from .views import  list_books, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    path('list_books', list_books,name='list_books' ),
    path('library/<str:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]