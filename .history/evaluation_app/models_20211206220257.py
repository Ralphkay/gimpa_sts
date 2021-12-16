from django.db import models

# Create your models here.


class Evaluation(models.Model):
    pass


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)