from django.shortcuts import render, redirect
from .forms import CustomUserCreationFor, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile

 

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