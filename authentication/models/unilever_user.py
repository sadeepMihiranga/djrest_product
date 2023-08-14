from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UnileverUser(AbstractUser):
    fav_color = models.CharField(blank=True, max_length=120)
    contact_no = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, null=False, blank=False, default='ACTIVE')
