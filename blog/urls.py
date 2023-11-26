from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("about-me", views.about_me, name="about_me"),
    path("posts", views.get_info_all_posts, name="all_posts"),
    path("posts/<slug:slug>", views.DetailPostView.as_view(), name="post_details"),
    path(
        "hashtags/<slug:slug>",
        views.DetailHashtagView.as_view(),
        name="hashtag_details",
    ),
]
