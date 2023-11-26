from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from .models import Post, Hashtag, Gallery


def main_page(request):
    posts = list(Post.objects.order_by("-date"))
    context = {
        "posts": posts[:3],
        "image": Gallery.objects.get(slug="main-page"),
    }
    return render(request, "blog/main_page.html", context)


def about_me(request):
    context = {"image": Gallery.objects.get(slug="about-me")}
    return render(request, "blog/about_me.html", context)


def get_info_all_posts(request):
    context = {"posts": Post.objects.order_by("-date")}
    return render(request, "blog/list_post.html", context)


class DetailPostView(DetailView):
    template_name = "blog/one_post.html"
    model = Post
    context_object_name = "sign_post"


class DetailHashtagView(DetailView):
    template_name = "blog/one_hashtag.html"
    model = Hashtag
