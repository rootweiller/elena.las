from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return '{0}'.format(self.email)


class Subjects(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    quota = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone = models.CharField(max_length=80, null=True, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.PROTECT)

    def __str__(self):

        return self.phone
