from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# This view lists books filtered by query parameter 'q' if provided
# Only accessible by users with 'can_view' permission in 'bookshelf' app
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Get search query from URL ?q= parameter, default empty string means all books
    query = request.GET.get('q', '')
    # Filter Books whose title contains the query string (case-insensitive)
    books = Book.objects.filter(title__icontains=query)
    # Render the book list template and send 'books' as context
    return render(request, 'bookshelf/book_list.html', {'books': books})
