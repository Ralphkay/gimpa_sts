from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):

    choices = (
                    ('100','Level 100'),
                    ('200','Level 200'),
                    ('300','Level 300'),
                    ('400','Level 400'),
                    ('600','Level 600'),
                    ('700','Level 700'),
                )
    user = models.OneToOneField(User,blank=False, null=False, on_delete=models.CASCADE)
    program = models.ForeignKey('evaluation_app.Program', blank=False, null=False, on_delete=models.PROTECT)
    level = models.CharField(max_length=30,choices=choices, null=False, blank=False)
    
    def __str__(self):
        return self.user.username
