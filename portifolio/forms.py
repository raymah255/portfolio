from . models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["post", "content", "parent"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"