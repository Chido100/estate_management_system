from django.urls import path
from . import views


urlpatterns = [
    path('send/', views.send_mail, name='send-mail'),
    path('inbox/', views.inbox, name='inbox'),
]
