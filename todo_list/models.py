from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PRIORITY = [
    ('LOW', 'LOW'),
    ('MEDIUM', 'MEDIUM'),
    ('HIGH', 'HIGH')
]
class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices = PRIORITY)
    is_complete = models.BooleanField(default=False)