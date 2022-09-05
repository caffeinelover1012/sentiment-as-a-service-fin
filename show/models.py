from django.db import models

# Create your models here.
from django.conf import settings

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Assoccount(models.Model):
    count = models.IntegerField()
