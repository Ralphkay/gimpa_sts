from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Student(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']


class QualityAssuranceAdmin(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']