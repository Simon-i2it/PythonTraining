import random

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
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


def index(request: HttpRequest):
    return render(
        request,
        "challenges/index.html",
        {"months": list(monthly_challenges.keys())},
    )


def get_monthly_challenge_str(request: HttpRequest, month: str):
    if month in monthly_challenges:
        challenge = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"month": month, "challenge": challenge},
        )
    else:
        return month_not_found(month)


def get_monthly_challenge_int(request: HttpRequest, month: int) -> HttpResponse:
    response: HttpResponse = HttpResponseNotFound(month_not_found(month))

    monthly_challenges_by_number = {
        index + 1: value for index, value in enumerate(monthly_challenges.keys())
    }

    if month in monthly_challenges_by_number:
        month_str = monthly_challenges_by_number[month]
        redirect_path = reverse("get_monthly_challenge_str", args=[month_str])
        return redirect(redirect_path)
    else:
        return month_not_found(month)


def month_not_found(month) -> HttpResponse:
    return HttpResponseNotFound(f"Month '{month}' is not found")
