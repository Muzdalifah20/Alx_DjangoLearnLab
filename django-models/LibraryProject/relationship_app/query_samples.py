from .models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        return books
    except Author.DoesNotExist:
        return []
    
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name= library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []

def library_librarian(library_name):
    try:
        library = Library.objects.get(name = library_name)
        librarian =  Librarian.objects.get(library)
        return librarian
    except library.DoesNotExist:
        return []
