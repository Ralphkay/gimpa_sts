from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

choices = (
    (o,'Poor'),
    (1,'Poor'),
    (2,'Poor'),
    (3,'Poor'),
    (,'Poor'),
)

class Evaluation(models.Model):
    pass

class Curriculum(models.Model):
    feedback_1 = models.CharField(max_length=200)
    feedback_1 = models.CharField(max_length=200)
    feedback_1 = models.CharField(max_length=200)
    feedback_1 = models.CharField(max_length=200)
    feedback_1 = models.CharField(max_length=200)




