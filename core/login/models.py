from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     role_choices = (
#         ('client', 'Client'),
#         ('staff', 'Staff'),
#     )
#     role = models.CharField(max_length=100, choices = role_choices)

# class client(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)

# class staff(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     depart_name = models.CharField(max_length=150)