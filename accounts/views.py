from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from a_posts.forms import ReplyCreateForm
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
        profile = get_object_or_404(CustomUser, username=username)
    elif request.user.is_authenticated:
        profile = request.user
    else:
        raise Http404("Sahifa topilmadi")


    posts = profile.posts.all()

    if request.htmx:
        if 'top-posts' in request.GET:
            posts = profile.posts.annotate(likes_count=Count('likes')).filter(likes_count__gt=0).order_by('-likes_count')
        elif 'top-comments' in request.GET:
            comments = profile.comments.annotate(likes_count=Count('likes')).filter(likes_count__gt=0).order_by('-likes_count')
            reply_form = ReplyCreateForm()
            return render(request, 'snippets/loop_profile_comments.html', {'comments': comments, "replyform": reply_form})
        elif 'liked-posts' in request.GET:
            posts = profile.likedposts.order_by('-likedpost__created')

        return render(request, 'snippets/loop_profile_posts.html', {'posts': posts})

    context = {
        "profile": profile.profile,
        "posts": posts
    }

    return render(request, 'a_users/profile.html', context)

@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("userprofile", username=request.user.username)  # Profilga qaytish


    return render(request, 'a_users/profile_edit.html', {'form': form})

@login_required
def profile_delete_view(request):
    if request.method == "POST":
        request.user.delete()
        logout(request)
        messages.success(request, "Account deleted")
        return redirect("home")

    return render(request, 'a_users/profile_delete.html')

