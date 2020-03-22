from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=10)
    flat = models.CharField(max_length=10, blank=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE,related_name="user_addresses")

# Create your models here.
