from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

