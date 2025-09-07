from django.urls import path
from .views import  books, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    path('books', books,name='books' ),
    path('library/<str:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]