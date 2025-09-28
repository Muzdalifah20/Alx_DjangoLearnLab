# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from rest_framework import permissions
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# from .models import Book
# from .serializers import BookSerializer
# from rest_framework import viewsets, permissions

# class BookViewSet(viewsets.ModelViewSet):
#     """
#     A ModelViewSet for managing Book instances through the API.

#     Provides the following actions automatically:
#     - list: Retrieve all Book instances (read-only).
#     - retrieve: Get details of a single Book by ID.
#     - create: Add a new Book instance.
#     - update: Modify an existing Book instance.
#     - partial_update: Partially update fields of a Book.
#     - destroy: Delete a Book instance.

#     Permission Policy:
#     - Read operations (list and retrieve) are openly accessible (AllowAny).
#     - Write operations (create, update, partial_update, destroy) are restricted to authenticated users.

#     This is enforced with the IsAuthenticatedOrReadOnly permission class.
#     """

#     queryset = Book.objects.all()     
#     serializer_class = BookSerializer    
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class BookListView(ListView):
#     model = Book
#     template_name = 'book_list.html'

# class BookListView(ListAPIView):
#     """
#     View to list all books.
#     Allows public access (no login required).
#     Renders 'book_list.html' template with 'object_list' context.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.AllowAny]

# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book_detail.html'

# class BookDetailView(RetrieveAPIView):
#     """
#     View to display details of a single book by ID.
#     Allows public access.
#     Renders 'book_detail.html' template with 'object' context.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.AllowAny]

# class BookCreateView(LoginRequiredMixin, CreateView):
#     model = Book
#     fields = ['title', 'publication_year', 'author']
#     template_name = 'book_form.html'
#     success_url = reverse_lazy("book_list")

#     def form_valid(self, form):
#         return super().form_valid(form)

# class BookCreateView(CreateAPIView):
#     """
#     View for adding a new book.
#     Requires user to be logged in.
#     Uses 'book_form.html' template.
#     Redirects to book list on success.
#     Custom form_valid overridden to add hooks for additional processing if needed.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class BookUpdateView(LoginRequiredMixin,UpdateView):
#     model = Book
#     fields = ['title', 'publication_year', 'author']
#     template_name = "book_form.html"
#     success_url = reverse_lazy('book_list') 

#     def form_valid(self, form):
#         return super().form_valid(form)

# class BookUpdateView(UpdateAPIView):
#     """
#     View for editing an existing book.
#     Requires user authentication.
#     Shares the 'book_form.html' template with create view.
#     Redirects to book list on success.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class BookDeleteView(DeleteView):
#     model = Book
#     template_name = 'book_confirm_delete.html'
#     success_url = reverse_lazy('book_list')

# class BookDeleteView(DestroyAPIView):
#     """
#     View for deleting a book.
#     Requires login.
#     Displays confirmation page 'book_confirm_delete.html'.
#     Redirects to book list after deletion.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books (GET)
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Lists all books.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]   

# Retrieve single book by ID (GET)
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/{id}/
    Retrieves the details of a specific book.
    Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book (POST)
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book.
    Requires user authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  

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
    permission_classes = [permissions.IsAuthenticated]

# Delete a book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/{id}/delete/
    Deletes a book.
    Requires user authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
