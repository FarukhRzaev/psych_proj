from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_info_all_posts, name="all_posts"),
    path("<str:slug_post>", views.get_info_one_post, name="post_details"),
]