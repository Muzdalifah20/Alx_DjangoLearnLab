from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library, Book, Author, Librarian
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required




def list_books(request):
    """Listing All books stored in the database"""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app:list_books')
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        # form handling code here
        # e.g., form = BookForm(request.POST)
        # if form.is_valid():
        #   form.save()
        pass  # placeholder
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # form = BookForm(request.POST, instance=book)
        # if form.is_valid():
        #    form.save()
        pass
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
