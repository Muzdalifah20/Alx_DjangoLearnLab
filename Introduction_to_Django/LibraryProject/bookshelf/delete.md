# Delete Book Instance

## Python Command

```python
from bookself.models import Book

book = book.objects.get(title = "Nineteen Eighty-Four")

book.delete()
books = Book.objects.all()

# Coonfirm deletion
print(books)
```

# Excepected output:

# <QuerySet []>
