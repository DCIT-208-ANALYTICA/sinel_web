from django import forms
from .models import Post, Page


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
            "id",
            'by',
            "created_at",
            "update_at",
        ]


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = [
            "id",
            'by',
            "slug",
            "created_at",
            "update_at",
        ]
