from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager


class User(AbstractUser):
    info = models.TextField(blank=True)
    objects = UserManager()