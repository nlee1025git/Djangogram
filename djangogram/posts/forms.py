from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {"caption", "image"}

        label = {
            "caption": "Content",
            "image": "Image",
        }

class CommentForm(forms.ModelForm):
    contents = forms.CharField(widget=forms.Textarea, label="")
    
    class Meta:
        model = Comment
        fields = ["contents"]