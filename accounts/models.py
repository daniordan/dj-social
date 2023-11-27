from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User, PermissionsMixin
from django.utils import timezone


# Create your models here.
class User(User, PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
