from django.db import models
from django.contrib.auth.models import User

from blog.models import BlogPost


class PostComment(models.Model):
    body = models.CharField(max_length=300)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField()
