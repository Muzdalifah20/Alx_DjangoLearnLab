from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents an author of books.
    Fields:
    - name: stores the author's full name as a string.
    
    This model is linked to the Book model with a one-to-many relationship,
    where one Author can have multiple Books.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """
    Represents a book written by an author.
    Fields:
    - title: the title of the book as a string.
    - publication_year: the year the book was published as an integer.
    - author: foreign key linking to the Author model, establishing a one-to-many relationship.
    
    The on_delete=models.CASCADE ensures that if an Author is deleted,
    all their books are also deleted automatically.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title