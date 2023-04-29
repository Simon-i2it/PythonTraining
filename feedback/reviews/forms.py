from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude=["rating"]
        labels = {
            "username": "Name",
        }
        error_messages = {
            "username": {
                "required": "Name must not be empty",
                "max_length": "Please enter a shorter name",
            }
        }
