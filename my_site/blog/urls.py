from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome),
    path("welcome/", views.welcome, name="url_welcome"),
    path("posts/", views.posts, name="url_posts"),
    path("posts/<slug:slug>", views.post, name="url_post"),
]
