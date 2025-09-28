from rest_framework import serializers
from .models import Author, Book
from datetime import date
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Serializes all fields from the Book model.
    
    Includes validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, data):
        """Function to ensure the publication date is nor in the fuure"""
        if data > date.today().year:
            raise serializers.ValidationError("The publication year can not be in the future")
        return data 


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    includes:
    'name' field from the author.
    A nested 'books' filed useing BookSerializer to dynamically serialize all related Book instances.
    This nested representation shows the relationship where one Author has many Books.
    The nested books are read-only to avoid changes via the Author serializer.
    """
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']