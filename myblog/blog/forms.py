# blog/forms.py
from django import forms
from .models import Post , Comment
from django.forms import DateInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user','title', 'content', 'published_at', 'image', 'category']
        widgets = {
            'published_at': DateInput(attrs={'type': 'date'}),
            'user': forms.HiddenInput()
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'content']
        widgets = {
            'user': forms.HiddenInput()            
        } 