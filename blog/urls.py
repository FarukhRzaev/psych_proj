from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main_page"),
    path("about-me/", views.AboutMe.as_view(), name="about_me"),
    path("posts/", views.AllPosts.as_view(), name="all_posts"),
    path("posts/<slug:slug>/", views.DetailPostView.as_view(), name="post_details"),
    path(
        "hashtags/<slug:slug>/",
        views.DetailHashtagView.as_view(),
        name="hashtag_details",
    ),
]
