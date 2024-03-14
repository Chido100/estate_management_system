from django import forms
from .models import CriticalAlert


class CriticalAlertForm(forms.ModelForm):
    class Meta:
        model = CriticalAlert
        fields = ['alert']
        