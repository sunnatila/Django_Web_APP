from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from a_posts.models import Post
from django.contrib.auth.models import AbstractUser

from accounts.models import CustomUser


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["url", "body", "tags"]
        labels = {
            "body": "Caption",
            'tags': 'Category'
        }
        widgets = {
            "body": forms.Textarea(attrs={'roes': 3, 'placeholder': "Add a caption...", 'class': 'font1 text-4xl'}),
            "url": forms.TextInput(attrs={"placeholder": "Add url..."}),
            'tags': forms.CheckboxSelectMultiple()
        }



class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            "body": "",
            'tags': 'Category'
        }

        widgets = {
            "body": forms.Textarea(attrs={"rows": 3, "class": 'font1 text-4xl'}),
            'tags': forms.CheckboxSelectMultiple()
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
