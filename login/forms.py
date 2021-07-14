from django import forms


# lable names has to be in sync with frontend labels
class SignUp(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    email = forms.CharField(label="email", max_length=30)
    password = forms.CharField(label="password", max_length=44)


class Login(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    password = forms.CharField(label="password", max_length=44)
