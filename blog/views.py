import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from blog.models import BlogPost
from comment.models import PostComment
from comment.forms import NewPostCommentForm
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
    if request.method == "POST":
        form = NewPostCommentForm(request.POST)
        if form.is_valid():
            comment = PostComment()
            comment.body = form.cleaned_data['body']
            comment.create_date = datetime.date.today()
            comment.author = request.user
            comment.blog = BlogPost.objects.get(pk=post_id)
            comment.save()
            messages.success(request, "Commented successfully.")
            return redirect("blog:view", post_id=post_id)
        messages.error(request, "There was invalid information in your form. Please review and try again.")
    else:
        comment_form = NewPostCommentForm()
        post = get_object_or_404(BlogPost, pk=post_id)
        comments = PostComment.objects.filter(blog__id=post.id)
        your_posts = BlogPost.objects.filter(author__id=request.user.id)
        return render(request, "blog/view.html", {"post": post, "comment_form": comment_form, "comments": comments, "your_posts": your_posts})    



def view_all_blog_posts(request):
    posts = BlogPost.objects.all()
    your_posts = BlogPost.objects.filter(author__id=request.user.id)
    return render(request, "blog/view_all.html", {"posts": posts, "your_posts": your_posts})