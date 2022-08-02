from django import forms

class ContactForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your first name"}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your last name"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "enter your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password"}))
    message  = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your message"}))
