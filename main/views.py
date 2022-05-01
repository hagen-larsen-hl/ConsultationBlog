from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from blog.models import BlogPost
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def landing(request):
    recent_posts = BlogPost.objects.all()[:4]
    popular_posts = BlogPost.objects.all()[:4]
    return render(request, "main/landing.html", {'recent_posts': recent_posts, 'popular_posts': popular_posts})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("landing")
    else:
        form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("landing")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    print(request.user)
    messages.info(request, "You have successfully logged out.") 
    return redirect("main:register")