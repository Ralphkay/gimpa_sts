from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class Evaluation(models.Model):
    pass


class Student(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)