from django import forms
from .models import Book

# ModelForm to create or edit Book instances securely
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# ExampleForm with manual fields, can be used for other input forms
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')
