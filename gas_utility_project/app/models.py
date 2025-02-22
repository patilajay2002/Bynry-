from django.db import models

# Create your models here.
from django.contrib.auth.models import User

SERVICE_CHOICES = [
    ('repair', 'Repair'),
    ('installation', 'Installation'),
    ('maintenance', 'Maintenance'),
]

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('resolved', 'Resolved'),
]

class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests')
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.service_type} - {self.status}"