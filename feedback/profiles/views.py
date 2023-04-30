from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from profiles.forms import ProfileForm
from profiles.models import Profile

# Create your views here.


class ProfileView(CreateView):
    template_name = "profiles/profile.html"
    form_class = ProfileForm
    success_url = "/profile/all"
    # success_url = reverse("url-profiles")  # why not reverse() ?


class ProfilesView(ListView):
    template_name = "profiles/profiles.html"
    context_object_name = "profiles"
    model = Profile
