from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

choices = (
    (o,'Poor'),
    (o,'Poor'),
    (o,'Poor'),
    (o,'Poor'),
)

class Evaluation(models.Model):
    pass

class Curriculum(models.Model):
    feedback_1 = models.CharField(max_length=200)
    feedback_1 = models.CharField(max_length=200)
    feedback_1 = models.CharField(max_length=200)
    feedback_1 = models.CharField(max_length=200)
    feedback_1 = models.CharField(max_length=200)




