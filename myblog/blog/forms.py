# blog/forms.py
from django import forms
from .models import Post , Comment
from django.forms import DateInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published', 'published_at', 'image', 'category']
        widgets = {
            'published_at': DateInput(attrs={'type': 'date'})
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']