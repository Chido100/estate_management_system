from django.db import models
from users.models import User


INCIDENT_STATUS = (
    ('pending', 'Pending'),
    ('in-progress', 'In-Progress'),
    ('completed', 'Completed'),
)

class IncidentReporting(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='incident_report', null=True, blank=True)
    reporter = models.ForeignKey(User, related_name='report_incident', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    assignee = models.ForeignKey(User, related_name='assigned_to', on_delete=models.CASCADE)
    is_resolved = models.BooleanField(default=False)
    date_accepted = models.DateTimeField(null=True, blank=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    incident_status = models.CharField(max_length=20, choices=INCIDENT_STATUS)


    class Meta:
        verbose_name_plural = 'Incident Reporting'


    def __str__(self):
        return self.subject
