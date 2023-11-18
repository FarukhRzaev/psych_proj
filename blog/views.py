from django.shortcuts import render, get_object_or_404
from random import sample
from .models import Post


def main_page(request):
    posts = list(Post.objects.all())
    context = {"posts": sample(posts, 4)}
    return render(request, "blog/main_page.html", context)


def get_info_all_posts(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/main_page.html", context)


def get_info_one_post(request, slug_post):
    post = get_object_or_404(Post, slug=slug_post)
    return render(request, "blog/one_post.html", {"sign_post": post})
