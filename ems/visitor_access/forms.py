from django import forms
from .models import VisitorAccessRequest


class VisitorAccessRequestForm(forms.ModelForm):
    class Meta:
        model = VisitorAccessRequest
        fields = ['visitor_name', 'gender', 'vehicle_registration', 'additional_information']
