from django.db import models
import uuid
from users.models import User



STATUS_CHOICES = (
    ('active', 'Active'),
    ('completed', 'Completed'),
    ('pending', 'Pending')
)

GENDER_CHOICES = (
    ('', 'Select gender'),
    ('male', 'Male'),
    ('female', 'Female')
)

class VisitorAccessRequest(models.Model):
    request_number = models.UUIDField(default=uuid.uuid4)
    visitor_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    vehicle_registration = models.CharField(max_length=20, blank=True, null=True)
    additional_information = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    date_created = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(null=True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    request_status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = 'Visitor Access Request'

    def __str__(self):
        return self.creator
