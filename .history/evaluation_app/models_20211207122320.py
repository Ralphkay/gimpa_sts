from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class Evaluation(models.Model):
    pass

class Curriculum(models.Model):
    feadback_1 = models.CharField(max_length=200)



