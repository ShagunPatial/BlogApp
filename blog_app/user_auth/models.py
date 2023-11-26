from django.db import models
from django.contrib.auth.models import AbstractUser


class TrackableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BgUser(AbstractUser, TrackableMixin):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
