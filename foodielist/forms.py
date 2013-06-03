from django.forms import ValidationError
from django.forms.models import ModelForm
from django import forms
from models import Foodie


class FoodieForm(ModelForm):
    """
    Custom model form for foodies.  Does additional validation to make sure
    foodies are only coming from disney email addresses
    """
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.lower().endswith("disney.com"):
            raise ValidationError("Disney email required")
        return email

    class Meta:
        model = Foodie
        exclude = ("joined",)


class UnsubscribeForm(forms.Form):
    """
    Simple email form field
    """
    email = forms.EmailField()