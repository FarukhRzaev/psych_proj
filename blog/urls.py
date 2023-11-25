from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("posts", views.get_info_all_posts, name="all_posts"),
    path("posts/<str:slug_post>", views.get_info_one_post, name="post_details"),
    path(
        "hashtags/<slug:slug>",
        views.DetailHashtagView.as_view(),
        name="hashtag_details",
    ),
]
