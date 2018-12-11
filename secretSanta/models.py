# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

from encrypted_model_fields.fields import EncryptedCharField


class CustomUser(AbstractUser):
    # add additional fields in here
    secret_santa_of = EncryptedCharField(max_length=128,null="True")
    def __str__(self):
        return self.email
    pass