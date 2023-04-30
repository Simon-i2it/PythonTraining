from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView

from profiles.forms import ProfileForm
from profiles.models import Profile

# Create your views here.


class ProfileView(CreateView):
    template_name = "profiles/profile.html"
    form_class = ProfileForm
    success_url = "/profile/create"
