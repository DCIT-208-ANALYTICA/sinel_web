from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from .models import Post


class PostsView(View):
    template_name = "blog/posts.html"

    def get(self, request, *args, **kwargs):
        context = {
            "posts": Post.objects.filter(visible=True).order_by("-id"),
            "recent_posts":
            Post.objects.filter(visible=True).order_by("-id")[:10]
        }
        return render(request, self.template_name, context)


class PostDetail(View):
    template_name = "blog/post_detail.html"

    def get(self, request, post_id, *args, **kwargs):
        context = {
            "post": get_object_or_404(Post, id=post_id),
            "recent_posts":
            Post.objects.filter(visible=True).order_by("-id")[:10]
        }
        return render(request, self.template_name, context)
