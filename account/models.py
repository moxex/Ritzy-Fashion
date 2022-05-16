from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    gender = models.CharField(choices=GENDER, max_length=10, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} {self.email}'