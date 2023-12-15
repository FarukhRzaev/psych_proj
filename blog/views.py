from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from .models import Post, Hashtag, Gallery


class MainPage(ListView):
    template_name = "blog/main_page.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.order_by("-date")[:3]
        return filter_qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image"] = Gallery.objects.get(slug="main-page")
        return context


class AboutMe(TemplateView):
    template_name = "blog/about_me.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image"] = Gallery.objects.get(slug="about-me")
        return context


class AllPosts(ListView):
    template_name = "blog/list_post.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.order_by("-date")
        return filter_qs


class DetailPostView(DetailView):
    template_name = "blog/one_post.html"
    model = Post
    context_object_name = "sign_post"


class DetailHashtagView(DetailView):
    template_name = "blog/one_hashtag.html"
    model = Hashtag
