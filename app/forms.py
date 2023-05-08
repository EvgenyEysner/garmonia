from django import forms
from django.core import validators


class EmailPostForm(forms.Form):
    first_name = forms.CharField(max_length=128, required=True)
    last_name = forms.CharField(max_length=128, required=True)
    email = forms.EmailField(
        required=True,
        validators=[
            validators.EmailValidator(
                message="Bitte geben Sie eine valide Email Adresse ein"
            )
        ],
    )
    subject = forms.CharField(max_length=64, required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)


class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=256)
    email = forms.EmailField()
    phone = forms.CharField(max_length=64)
    package = forms.Select()
