from django import forms

class UploaderFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    