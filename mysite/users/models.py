from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.utils import timezone
from jsonfield import JSONField

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class video(models.Model):
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    # videoUrl = models.CharField(max_length = 40) # we input the url // figure out max length later
    author = models.CharField(max_length = 20) # user id 
    timestamp = models.DateTimeField(auto_now = True)
    expectedCount = models.IntegerField(validators = [MinValueValidator(0)], default = 0)
