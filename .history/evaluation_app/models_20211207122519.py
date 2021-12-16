from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

choices = (
    (1,'Poor'),
    (2,'Okay'),
    (3,'Good'),
    (4,'Very Good'),
    (5,'Excellent'),
)

class Evaluation(models.Model):
    Curriculum

class Curriculum(models.Model):
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices)
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices)
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices)
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices)
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices)




