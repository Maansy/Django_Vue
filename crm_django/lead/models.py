from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Lead(models.Model):

    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'

    CHOISES_STATES = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'Inprogress'),
        (LOST, 'Lost'),
        (WON, 'Won'),
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOISES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=225)
    website = models.CharField(max_length=225, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=25, choices=CHOISES_STATES, default=NEW)
    priority = models.CharField(
        max_length=25, choices=CHOISES_PRIORITY, default=MEDIUM)
    created_by = models.ForeignKey(
        User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.company
