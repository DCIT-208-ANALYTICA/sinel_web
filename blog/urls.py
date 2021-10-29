from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("posts", views.PostsView.as_view(), name="posts"),
    path("post_detail", views.PostDetail.as_view(), name="post_detail"),
]
