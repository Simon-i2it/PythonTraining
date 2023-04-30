from django import forms


class ProfileForm(forms.Form):
    image_file = forms.FileField()
