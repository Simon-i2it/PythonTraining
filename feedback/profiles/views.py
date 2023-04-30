from django.views.generic.edit import CreateView

from profiles.forms import ProfileForm

# Create your views here.


class ProfileView(CreateView):
    template_name = "profiles/profile.html"
    form_class = ProfileForm
    success_url = "/profile/create"
