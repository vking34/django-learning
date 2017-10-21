# from django import forms
# from django.core import validators
#
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100, validators=[validators.validate_slug])
#     password = forms.CharField(widget=forms.PasswordInput())
#


from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())