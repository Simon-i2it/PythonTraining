from django import forms

from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            "image_file": "",
        }
