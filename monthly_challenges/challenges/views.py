import random

from django.urls import reverse
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)

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


def get_monthly_challenges(month: str):
    if month in monthly_challenges:
        return HttpResponse(monthly_challenges[month])
    else:
        return month_not_found(month)


def month_not_found(month) -> HttpResponse:
    return HttpResponseNotFound(f"Month '{month}' is not found")


def january(request: HttpRequest):
    return get_monthly_challenges("january")


def february(request: HttpRequest):
    return get_monthly_challenges("february")


def get_challenge(request: HttpRequest, month: str) -> HttpResponse:
    response: HttpResponse = month_not_found(month)
    if month == "january":
        response = january(request)
    elif month == "february":
        response = february(request)
    else:
        response = get_monthly_challenges(month)
    return response


def get_challenge_by_month_number(request: HttpRequest, month: int) -> HttpResponse:
    response: HttpResponse = HttpResponseNotFound(month_not_found(month))

    monthly_challenges_by_number = {
        i + 1: value for i, value in enumerate(monthly_challenges.keys())
    }

    if month in monthly_challenges_by_number:
        redirect_path = reverse("get_challenge_str", args=[monthly_challenges_by_number[month]])
        return HttpResponseRedirect(redirect_path)
    else:
        return month_not_found(month)
