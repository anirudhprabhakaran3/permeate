from django import forms
from django.forms import fields
from .models import Comments, Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'tags']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']