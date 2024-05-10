from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class RegisterResidentForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'full_name', 'house_number', 'street_name', 'phone_number', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'house_number', 'street_name']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['image']
        
