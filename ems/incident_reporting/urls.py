from django.urls import path
from . import views


urlpatterns = [
    path('incident_report_details/<int:pk>/', views.incident_report_details, name='incident-report-details'),
    path('new_incident/', views.new_incident, name='new-incident'),
    path('update_incident/<int:pk>/', views.update_incident, name='update-incident'),
    path('all_reported_incidents/', views.all_reported_incidents, name='all-reported-incidents'),
    path('report_queue/', views.report_queue, name='report-queue'),
    path('accept_incident_report/<int:pk>/', views.accept_incident_report, name='accept-incident-report'),
    path('close_incident_report/<int:pk>/', views.close_incident_report, name='close-incident-report'),
    path('report_in_progress/', views.report_in_progress, name='report-in-progress'),
    path('all_resolved_reports/', views.all_resolved_reports, name='all-resolved-reports'),
]