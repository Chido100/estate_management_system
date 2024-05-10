from django.shortcuts import render, redirect, get_object_or_404
from .models import Dues
from .forms import DuesForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Payment imports
from decimal import Decimal
import stripe
from django.conf import settings




# Make dues payment
@login_required
def pay_dues(request):
    if request.method == 'POST':
        form = DuesForm(request.POST)
        if form.is_valid():
            due_payment = form.save(commit=False)
            due_payment.creditor = request.user
            due_payment.save()
            return redirect('create-checkout-session', pk=due_payment.pk)
    else:
        form = DuesForm()
    return render(request, 'dwell_dues/pay_dues.html', {'form': form})


@login_required
def pay_dues_details(request, pk):
    pay_due = get_object_or_404(Dues, pk=pk)
    return render(request, 'dwell_dues/pay_dues_details.html', {'pay_due': pay_due})


@login_required
def dues_history(request):
    all_dues = Dues.objects.all()
    return render(request, 'dwell_dues/dues_history.html', {'all_dues': all_dues})



