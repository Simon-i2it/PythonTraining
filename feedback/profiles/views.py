from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

# Create your views here.


class ProfileView(View):
    def get(self, request):
        return render(request, "profiles/profile.html")

    def post(self, request: HttpRequest):
        print(request.FILES["image"])
        with open("profiles/temp/image.jpg", "wb+") as destination:
            for chunk in request.FILES["image"].chunks():
                destination.write(chunk)
        return redirect("/profile")
