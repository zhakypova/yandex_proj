from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telegram_chat_id = models.IntegerField(blank=True, null=True)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_chat_id = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.user.username
