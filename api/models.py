import datetime

from django.db import models

from django.utils import timezone

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=255)
    no_action_price = models.IntegerField()
    action_price = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUSES = (
        ('IsProcess', 'IsProcess'),
        ('Completed', 'Completed'),
    )

    phone = models.CharField(max_length=18)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=10, choices=STATUSES, null=True, default=STATUSES[0])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.service_id} {self.service.name}"