from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class DriverUser(AbstractUser):
    name = models.CharField(_("name"), max_length=250)

    def __str__(self):
        return self.username
