from django import forms
from django.core import validators

class UploaderFileForm(forms.Form):
    title = forms.CharField(max_length=50, validators=[validators.validate_slug])
    file = forms.FileField()


    