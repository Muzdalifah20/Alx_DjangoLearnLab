from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views  


app_name = 'relationship_app'

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('library/<str:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]
