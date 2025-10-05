from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CustomUserCreationFor, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Post
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
        
