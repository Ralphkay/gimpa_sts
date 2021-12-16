from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

choices = (
    ('1','Poor'),
    ('2','Okay'),
    ('3','Good'),
    ('4','Very Good'),
    ('5','Excellent'),
)

class Evaluation(models.Model):
    curriculum_computed_value = models.FloatField(default=0, editable=False)
    punctuality_computed_value = models.FloatField(default=0, editable=False)
    aggregated_score_computed_value = models.FloatField(default=0, editable=False)

class Curriculum(models.Model):
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_2 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_3 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_4 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_5 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    
    def save


class Punctuality(models.Model):
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_2 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_3 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_4 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_5 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')




