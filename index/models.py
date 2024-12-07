from django.db import models
from djangondor.models import BaseTimestampModel, NULLABLE, NULLABLE_CHARFIELD
from django.db.models import (
    CharField,
    IntegerField,
    FloatField,
    ForeignKey,
    ManyToManyField,
    OneToOneField,
    EmailField
)
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email=EmailField(max_length=255,unique=True)

