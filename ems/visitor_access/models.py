from django.db import models
import random
import string
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

# Generate random code to use as Visitor Access Code
def generate_access_code():
    """Generate a random 5-character access code."""
    pass_code = ''.join(random.choices(string.digits, k=5))
    return pass_code


class VisitorAccessRequest(models.Model):
    access_code = models.CharField(max_length=5, unique=True, default=generate_access_code)
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
        return self.visitor_name
