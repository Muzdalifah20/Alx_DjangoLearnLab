# Create a Book Instance

## Python Command

```python
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
```

# Retrive book Atribute

## Python Command

```python
book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.publication_year)
```

# expected output:

# 1984

# George Orwell

# 1949

# Update book

## Python Command

```python
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
```

# Nineteen Eighty-Four

# Delete Book Instance

## Python Command

```python
book.delete()
books = Book.objects.all()

# Coonfirm deletion
print(books)
```

# Excepected output:

# <QuerySet []>
