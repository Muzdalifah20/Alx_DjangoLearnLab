# Delete Book Instance

## Python Command

```python
from bookshelf.models import Book


book = Book.objects.get(title = "Nineteen Eighty-Four")

book.delete()
books = Book.objects.all()

# Coonfirm deletion
print(books)
```

# Excepected output:

# <QuerySet []>
