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
    curriculum = models.OneToOneField('Curriculum', on_delete=models.CASCADE, primary_key=True)
    punctuality = models.OneToOneField('Punctuality', on_delete=models.CASCADE)
    aggregated_score = models.FloatField(default=0, editable=False)

class Curriculum(models.Model):
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices, def``)
    feedback_2 = models.CharField(max_length=200, blank=False,null=False, choices=choices, def``)
    feedback_3 = models.CharField(max_length=200, blank=False,null=False, choices=choices, def``)
    feedback_4 = models.CharField(max_length=200, blank=False,null=False, choices=choices, def``)
    feedback_5 = models.CharField(max_length=200, blank=False,null=False, choices=choices, def``)


class Punctuality(models.Model):
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices)
    feedback_2 = models.CharField(max_length=200, blank=False,null=False, choices=choices)
    feedback_3 = models.CharField(max_length=200, blank=False,null=False, choices=choices)
    feedback_4 = models.CharField(max_length=200, blank=False,null=False, choices=choices)
    feedback_5 = models.CharField(max_length=200, blank=False,null=False, choices=choices)



