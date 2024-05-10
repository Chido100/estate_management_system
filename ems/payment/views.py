from django.shortcuts import render, redirect, get_object_or_404
from dwell_dues.models import Dues
from dwell_dues.forms import DuesForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Payment imports
from decimal import Decimal
import stripe
from django.conf import settings




# Stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def create_checkout_session(request, pk):
    due = get_object_or_404(Dues, pk=pk)
    if request.method == 'POST':
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': due.amount,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('payment-completed')),
                cancel_url=request.build_absolute_uri(reverse('payment-cancelled')),
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)
    return render(request, 'payment/create_checkout_session.html', {'due': due})



def payment_completed(request):
    return render(request, 'payment/payment_completed.html')


def payment_cancelled(request):
    return render(request, 'payment/payment_cancelled.html')
