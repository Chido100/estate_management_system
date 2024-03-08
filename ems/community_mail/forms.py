from django import forms
from .models import CommunityMail


class CommunityMailForm(forms.ModelForm):
    class Meta:
        model = CommunityMail
        fields = ['receiver', 'content']

        