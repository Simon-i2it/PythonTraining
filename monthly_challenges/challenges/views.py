import random

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

monthly_challenges = {
    "january": f"Read {random.randint(5, 20)} books",
    "february": f"Write {random.randint(5, 10)} pages every day",
    "march": f"Practice {random.randint(30, 60)} minutes of meditation every day",
    "april": f"Learn a new skill for {random.randint(15, 30)} minutes every day",
    "may": f"Take {random.randint(5, 10)} photos and edit them",
    "june": f"Complete {random.randint(20, 30)} hours of physical exercise",
    "july": f"Try a new recipe every day",
    "august": f"Journal for {random.randint(10, 20)} minutes every day",
    "september": f"Listen to {random.randint(20, 30)} new songs",
    "october": f"Write {random.randint(500, 1000)} words every day",
    "november": f"Complete {random.randint(15, 20)} hours of community service",
    "december": f"Learn a new language for {random.randint(15, 30)} minutes every day",
}

print(monthly_challenges)


def january(request: HttpRequest):
    return HttpResponse(monthly_challenges["january"])


def february(request: HttpRequest):
    return HttpResponse(monthly_challenges["february"])


def march(request: HttpRequest):
    return HttpResponse(monthly_challenges["march"])


def get_challenge(request: HttpRequest, month: str) -> HttpResponse:
    response = None
    if month == "january":
        response = january(request)
    elif month == "february":
        response = february(request)
    elif month == "march":
        response = march(request)
    else:
        try:
            return HttpResponse(monthly_challenges[month])
        except:
            return HttpResponseNotFound(f"Month '{month}' is not supported yet")
    return response


def get_challenge_by_month_number(request: HttpRequest, month: int) -> HttpResponse:
    response = None
    if month == 1:
        response = january(request)
    elif month == 2:
        response = february(request)
    elif month == 3:
        response = march(request)
    else:
        return HttpResponseNotFound(f"Month '{month}' is not supported yet")
    return response
