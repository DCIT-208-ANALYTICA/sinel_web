from django.shortcuts import render
from django.views.generic import View


class PostsView(View):
    template_name = "blog/posts.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)

class PostDetail(View):
    template_name = "blog/post_detail.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)
