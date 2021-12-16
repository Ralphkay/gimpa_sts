from django.db import models
from django.contrib.auth
# Create your models here.


class Evaluation(models.Model):
    pass


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)