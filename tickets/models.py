from django.db import models
from users.models import User, Category


# Create your models here.
class Ticket(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    )
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_tickets')
    operator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='operator_tickets')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='new', max_length=50)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='low', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)