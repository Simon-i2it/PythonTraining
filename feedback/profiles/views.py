from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from profiles.forms import ProfileForm
from profiles.models import Profile

# Create your views here.


class ProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/profile.html", {"form": form})

    def post(self, request: HttpRequest):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = Profile(image_file=request.FILES["image_file"])
            profile.save()
        return render(request, "profiles/profile.html", {"form": submitted_form})
