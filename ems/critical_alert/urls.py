from django.urls import path
from . import views


urlpatterns = [
    path('send_alert/', views.send_alert, name='send-alert'),
    path('alert_history/', views.alert_history, name='alert-history'),
]