from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
            "id",
            'by',
            "created_at",
            "update_at",
        ]
