from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Create your views here.

def books(request):
    """Listing All books stored in the database"""
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'relationship_app/books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['books'] = self.object.books.all()
        return context
 