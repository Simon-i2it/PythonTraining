from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/welcome.html")


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/posts.html")


def post(request: HttpRequest, slug: str) -> HttpResponse:
    return render(request, "blog/post.html")
