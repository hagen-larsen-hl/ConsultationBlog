from django import forms
from .models import PostComment
import datetime


class NewPostCommentForm(forms.ModelForm):

    class Meta:
        model = PostComment
        fields = ("body",)
