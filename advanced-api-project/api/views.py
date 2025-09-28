from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
DjangoFilterBackend = rest_framework.DjangoFilterBackend

# List all books (GET)
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Lists all books.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]   

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields you can filter by exact match
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields to search text in (partial match)
    search_fields = ['title', 'author']

    # Fields allowed for ordering results
    ordering_fields = ['title', 'publication_year']

# Retrieve single book by ID (GET)
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/{id}/
    Retrieves the details of a specific book.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a new book (POST)
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book.
    Requires user authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        
        serializer.save()

# Update a book (PUT/PATCH)
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/{id}/update/
    Updates an existing book.
    Requires user authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete a book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/{id}/delete/
    Deletes a book.
    Requires user authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
