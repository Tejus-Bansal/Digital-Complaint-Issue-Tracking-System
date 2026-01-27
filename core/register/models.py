from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    role_choices = (
        ('client', 'Client'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=100, choices = role_choices)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    depart_name = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username