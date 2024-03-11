from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class RegisterResidentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'password1', 'password2', 'house_number', 'street_name']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'house_number', 'street_name']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['image']
        
