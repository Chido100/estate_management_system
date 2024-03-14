from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CriticalAlert
from .forms import CriticalAlertForm
from twilio.rest import Client
from django.conf import settings
from decouple import config
from users.models import User



def send_alert(request):
    if request.method == "POST":
        form = CriticalAlertForm(request.POST)
        if form.is_valid():
            alert_sender = form.save(commit=False)
            alert_sender.sender = request.user
            alert_sender.save()
            messages.warning(request, 'Alert sent!')
            return redirect('dashboard')
    else:
        form = CriticalAlertForm()
    return render(request, 'critical_alert/send_alert.html', {'form': form})










