from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, CustomUserCreationForm
from .models import CustomUser, Profile


def user_register_view(request):
    user_form = CustomUserCreationForm()
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return redirect('login')

    return render(request, "registration/sign_up.html", {"user_form": user_form})


def logout_view(request):
    logout(request)
    return redirect('home')


def profile_view(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)  # Profile mavjud bo'lmasa yaratish
    return render(request, 'a_users/profile.html', {"profile": user_profile})

def profile_edit_view(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)  # Profile yaratish agar mavjud bo'lmasa

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'a_users/profile_edit.html', {'form': form})

