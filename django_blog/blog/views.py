from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import CustomUserCreationFor, UserUpdateForm, ProfileUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


 

def register(request):
    if request.method == "POST":
        form = CustomUserCreationFor(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationFor()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile(request):
    user = request.user
    try:
        profile = user.profile
    except ObjectDoesNotExist:
        profile = Profile.objects.create(user=user)  # create profile if missing

    if request.method == "POST":
        updated_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if updated_form.is_valid() and profile_form.is_valid():
            updated_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        updated_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {'updated_form': updated_form, 'profile_form': profile_form}
    return render(request, 'profile.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_vlaid(self, form):
        form.instance.author = self.request.user
        return super().form_vlaid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class PostDeleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
        

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=post.id)
    else:
        form = CommentForm()
    return render(request, "comment_form.html", {'form': form})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden()
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "comment_form.html", {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden()
    post_id = comment.post.id
    if request.method == "POST":
        comment.delete()
        return redirect("post_detail", pk=post_id)
    return render(request, "comment_confirm_delete.html", {'comment': comment})

