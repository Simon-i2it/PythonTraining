from django import forms

from reviews.models import Review


class ReviewForm(forms.Form):
    # username = forms.CharField(
    #     label="Name",
    #     max_length=100,
    #     error_messages={
    #         "required": "Name must not be empty",
    #         "max_length": "Please enter a shorter name",
    #     },
    # )
    # feedback = forms.CharField(widget=forms.Textarea, max_length=2000)
    # rating = forms.IntegerField(min_value=1, max_value=5)

    class ReviewForm(forms.Form):
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