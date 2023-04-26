from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def posts(request: HttpRequest) -> HttpResponse:
    return HttpResponse()


def post(request: HttpRequest, slug: str) -> HttpResponse:
    return HttpResponse()
