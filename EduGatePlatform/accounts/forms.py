from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  
    confirm_password = forms.CharField(widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username', 'email']

    full_name = forms.CharField(max_length=150)
    national_id = forms.CharField(max_length=20)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField()  
    password = forms.CharField(widget=forms.PasswordInput)  
