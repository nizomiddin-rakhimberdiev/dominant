import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.utils import timezone

# Create your models here.
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()
    action_price = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class CategoryService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)


class Order(models.Model):
    STATUSES = (
        ('IsProcess', 'IsProcess'),
        ('Completed', 'Completed'),
    )

    phone = models.CharField(max_length=18)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=10, choices=STATUSES, null=True, default=STATUSES[0])
    offera = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.service_id} {self.service.name}"


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return f


class News(models.Model):
    photo = models.ImageField()
    time_update = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=300)
    subTitle = models.CharField(max_length=500)
    content = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=18)
    resume = models.FileField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class Consultation(models.Model):
    STATUSES = (
        ('IsProcess', 'IsProcess'),
        ('Completed', 'Completed'),
    )

    fullname = models.CharField(max_length=150)
    phone = models.CharField(max_length=18)
    status = models.CharField(max_length=10, choices=STATUSES, null=True, default=STATUSES[0])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone
