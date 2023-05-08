from django import forms


class EmailPostForm(forms.Form):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField()
    subject = forms.CharField(max_length=64)
    message = forms.CharField(required=True, widget=forms.Textarea)
