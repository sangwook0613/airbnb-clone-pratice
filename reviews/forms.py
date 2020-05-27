from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = (
            "review",
            "accuracy",
            "communication",
            "cleaniness",
            "location",
            "check_in",
            "value",
        )
