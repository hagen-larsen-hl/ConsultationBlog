from django import forms
from .models import BlogPost
import datetime


class NewBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ("title", "body")
