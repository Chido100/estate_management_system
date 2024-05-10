from django.urls import path
from . import views


urlpatterns = [
    path('create_checkout_session/<int:pk>/', views.create_checkout_session, name='create-checkout-session'),
    path('payment_completed/', views.payment_completed, name='payment-completed'),
    path('payment_cancelled/', views.payment_cancelled, name='payment-cancelled'),
]