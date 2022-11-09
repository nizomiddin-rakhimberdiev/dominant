from django.contrib.auth.models import AbstractUser
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(default='default_profile_pic.png')
    phone_number = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.phone_number

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

