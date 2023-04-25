from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404

# Create your views here.


def january(request: HttpRequest):
    return HttpResponse(f"Vegan for the entire month")


def february(request: HttpRequest):
    return HttpResponse(f"Taking a photo every day")


def march(request: HttpRequest):
    return HttpResponse(f"100 Pushups every day")


def get_challenge(request: HttpRequest, month) -> HttpResponse:
    response = None
    if month == "january":
        response = january(request)
    elif month == "february":
        response = february(request)
    elif month == "march":
        response = march(request)
    else:
        return HttpResponseNotFound(f"Month '{month}' is not supported yet")
    return response
