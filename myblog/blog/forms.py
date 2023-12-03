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
        
        
        
    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super(PostForm, self).__init__(*args, **kwargs)
        
        # Set the initial value for the 'user' field
        # Assuming that the current user is available in the view's request
        self.fields['user'].initial = self.initial.get('user', None)
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'content']
        widgets = {
            'user': forms.HiddenInput()            
        } 