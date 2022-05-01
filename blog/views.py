import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from blog.models import BlogPost
from .forms import NewBlogPostForm

# Create your views here.

def create_blog_request(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NewBlogPostForm(request.POST)
            if form.is_valid():
                post = BlogPost()
                post.title = form.cleaned_data['title']
                post.body = form.cleaned_data['body']
                post.create_date = datetime.date.today()
                post.author = request.user
                post.save()
                messages.success(request, "Posted successfully.")
                return redirect("landing")
            messages.error(request, "There was invalid information in your form. Please review and try again.")
        else:
            form = NewBlogPostForm()
        return render(request, "blog/create.html", {"form": form})
    else:
        return redirect("main:register")


def view_blog_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(BlogPost, pk=post_id)
        return render(request, "blog/view.html", {"post": post})
    else:
        return redirect("main:register")