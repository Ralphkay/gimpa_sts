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
    curriculum_computed_value = models.FloatField(default=0, editable=False)
    punctuality_computed_value = models.FloatField(default=0, editable=False)
    aggregated_score_computed_value = models.FloatField(default=0, editable=False)

class Curriculum(models.Model):
    
    class FeedbackChoices(models.IntegerChoices):
        POOR = 1
        GOOD = 2
        NEUTRAL = 3
        VERY_GOOD = 4
        EXCELLENT = 5
    
    feedback_1 = models.IntegerField(blank=False,null=False, choices=FeedbackChoices.choices, default=0)
    feedback_2 = models.IntegerField(blank=False,null=False, choices=FeedbackChoices.choices, default=0)
    feedback_3 = models.IntegerField(blank=False,null=False, choices=FeedbackChoices.choices, default=0)
    feedback_4 = models.IntegerField(blank=False,null=False, choices=FeedbackChoices.choices, default=0)
    feedback_5 = models.IntegerField(blank=False,null=False, choices=FeedbackChoices.choices, default=0)
    computed_value = models.FloatField(default=0, editable=False)
    
    def save(self, *args, **kwargs):
        self.computed = ((float(self.feedback_1) + float(self.feedback_2) + float(self.feedback_3) + float(self.feedback_4) + float(self.feedback_5))/5) * 100
        print(f"{self.feedback_1} )
        return super().save(*args, **kwargs)
        


class Punctuality(models.Model):
    feedback_1 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_2 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_3 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_4 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')
    feedback_5 = models.CharField(max_length=200, blank=False,null=False, choices=choices, default='0')




