from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("create/", views.create_blog_request, name="create"),
    path("view/<int:post_id>", views.view_blog_post, name="view"),
    path("view/all", views.view_all_blog_posts, name="view_all")
]