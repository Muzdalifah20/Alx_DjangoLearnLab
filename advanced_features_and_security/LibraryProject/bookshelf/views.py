from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm  # <-- Import your form here

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # process form.cleaned_data if needed
            return redirect('bookshelf:book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
