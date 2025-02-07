from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

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
    if username:
        # Username bo'yicha foydalanuvchini olish
        user = get_object_or_404(CustomUser, username=username)
    elif request.user.is_authenticated:
        # Agar username berilmagan bo'lsa, hozirgi foydalanuvchi profilini olish
        user = request.user
    else:
        raise Http404("Sahifa topilmadi")

    # Profilni signals orqali avtomatik yaratamiz, shuning uchun to'g'ridan-to'g'ri olish mumkin
    profile = get_object_or_404(Profile, user=user)

    return render(request, 'a_users/profile.html', {"profile": profile})

@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile", username=request.user.username)  # Profilga qaytish


    return render(request, 'a_users/profile_edit.html', {'form': form})

@login_required
def profile_delete_view(request):
    if request.method == "POST":
        request.user.delete()
        logout(request)
        messages.success(request, "Account deleted")
        return redirect("home")

    return render(request, 'a_users/profile_delete.html')

