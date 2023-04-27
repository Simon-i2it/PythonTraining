from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome),
    path("welcome/", views.welcome),
    path("posts/", views.posts),
    path("posts/<slug:slug>", views.post, name="path_post"),
]
