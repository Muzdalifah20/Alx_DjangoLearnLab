from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteview, add_comment, edit_comment, delete_comment

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteview.as_view(), name="post_delete"),
    path("post/<int:post_id>/comments/new/", add_comment, name="comment_add"),
    path("post/<int:comment_id>/edit/", edit_comment, name="comment_edit"),
    path("post/<int:comment_id>/deltet/", delete_comment, name="comment_delete"),

]