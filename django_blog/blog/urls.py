from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteview

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", PostDeleteview.as_view(), name="post_delete"),
]