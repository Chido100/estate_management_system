from django.urls import path
from . import views



urlpatterns = [
    path('access_request_details/<int:pk>/', views.access_request_details, name='access-request-details'),
    path('create_access_request/', views.create_access_request, name='create-access-request'),
    path('update_access_request/<int:pk>/', views.update_access_request, name='update-access-request'),
    path('all_access_requests/', views.all_access_requests, name='all-access-requests'),
    path('request_queue/', views.request_queue, name='request-queue'),
    path('accept_access_request/<int:pk>/', views.accept_access_request, name='accept-access-request'),
    path('close_access_request/<int:pk>/', views.close_access_request, name='close-access-request'),
    path('workspace/', views.workspace, name='workspace'),
    path('all_closed_requests/', views.all_closed_requests, name='all-closed-requests'),
]