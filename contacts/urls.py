from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContactView.as_view(), name="contacts"),
    path("success/", views.SuccessView.as_view()),
]
