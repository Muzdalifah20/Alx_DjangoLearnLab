from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView, register
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'relationship_app'

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('library/<str:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('accounts/signup/', register, name='register'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]
