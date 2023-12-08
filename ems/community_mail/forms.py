from django import forms
from .models import NewMail, ReplyMail



class NewMailForm(forms.ModelForm):
    class Meta:
        model = NewMail
        fields = ['subject', 'content']


class ReplyMailForm(forms.ModelForm):
    class Meat:
        model = ReplyMail
        fields = ['reply_message']
        