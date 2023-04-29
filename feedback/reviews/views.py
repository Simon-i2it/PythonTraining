from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.


def review(request: HttpRequest):
    if request.method == "POST":
        username = request.POST["username"]
        return redirect(thank_you, username)
    else:
        return render(request, "reviews/review.html")


def thank_you(request: HttpRequest, username: str):
    return render(request, "reviews/thank_you.html", {"username": username})
