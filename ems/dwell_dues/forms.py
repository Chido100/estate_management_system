from django import forms
from .models import Dues



class DuesForm(forms.ModelForm):
    class Meta:
        model = Dues
        fields = ['utility_bill', 'amount']
        