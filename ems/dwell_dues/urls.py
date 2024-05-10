from django.urls import path
from . import views



urlpatterns = [
    path('pay_dues/', views.pay_dues, name='pay-dues'),
    path('pay_dues_details/<int:pk>/', views.pay_dues_details, name='pay-dues-details'),
    path('dues_history/', views.dues_history, name='dues-history'),
]
