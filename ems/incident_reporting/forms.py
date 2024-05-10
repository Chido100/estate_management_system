from django import forms
from .models import IncidentReporting



class IncidentReportingForm(forms.ModelForm):
    class Meta:
        model = IncidentReporting
        fields = ['subject', 'content', 'image']