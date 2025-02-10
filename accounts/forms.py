from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            'realname': 'Name',

        }
        widgets = {
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows': 2})
        }



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']