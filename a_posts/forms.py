from django import forms
from django.forms import ModelForm

from a_posts.models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        labels = {
            "body": "Caption",
        }
        widgets = {
            "body": forms.Textarea(attrs={'roes': 3, 'placeholder': "Add a caption...", 'class': 'font1 text-4xl'})
        }

