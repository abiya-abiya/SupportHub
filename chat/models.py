from django.db import models

from tickets.models import Ticket
from users.models import User


# Create your models here.
class Message(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class TicketHistory(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    old_status = models.BooleanField(default=False)
    new_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)