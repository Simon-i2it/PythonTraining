from django.urls import path

from . import views

urlpatterns = [
    path("", views.posts,),
    path("posts", views.posts),
    path("posts/<slug:slug>", views.post, name="post_url"),
]