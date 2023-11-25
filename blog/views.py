from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from random import sample
from .models import Post, Hashtag


def main_page(request):
    posts = list(Post.objects.order_by("-date"))
    context = {"posts": sample(posts, 3)}
    return render(request, "blog/main_page.html", context)


def get_info_all_posts(request):
    context = {"posts": Post.objects.order_by("-date")}
    return render(request, "blog/list_post.html", context)


def get_info_one_post(request, slug_post):
    post = get_object_or_404(Post, slug=slug_post)
    return render(request, "blog/one_post.html", {"sign_post": post})


class DetailHashtagView(DetailView):
    template_name = "blog/one_hashtag.html"
    model = Hashtag
