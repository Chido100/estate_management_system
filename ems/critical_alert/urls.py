from django.urls import path
from . import views


urlpatterns = [
    path('send_alert/', views.send_alert, name='send-alert'),
]