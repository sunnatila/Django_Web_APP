from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

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


def profile_view(request, username=None):
    # Agar username parameteri bo'lsa, o'sha foydalanuvchining profilini olish
    if username:
        user = get_object_or_404(CustomUser, username=username)
        profile = get_object_or_404(Profile, user=user)  # Bu foydalanuvchining profilini olish
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404("Page not found")
        # Agar username bo'lmasa, hozirgi login qilingan foydalanuvchining profilini olish
        profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, 'a_users/profile.html', {"profile": profile})


@login_required
def profile_edit_view(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)  # Profil yaratish agar mavjud bo'lmasa

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'a_users/profile_edit.html', {'form': form})


@login_required
def profile_delete_view(request):
    if request.method == "POST":
        request.user.delete()
        logout(request)
        messages.success(request, "Account deleted")
        return redirect("home")

    return render(request, 'a_users/profile_delete.html')

