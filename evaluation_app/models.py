import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
# from django.utils import timezone
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify

from accounts.models import Student
import datetime


# Create your models here.

class FeedbackChoices(models.IntegerChoices):
    POOR = 1
    GOOD = 2
    NEUTRAL = 3
    VERY_GOOD = 4
    EXCELLENT = 5


class Evaluation(models.Model):
    """
    This model holds all evaluation submission after
    student has submitted evaluation 
    (It is a parent model of the Evaluation Submission model)
    @facilitator
    @course level
    """

    facilitator = models.ForeignKey('Facilitator', on_delete=models.CASCADE)
    course = models.OneToOneField('Course', on_delete=models.CASCADE)
    description = models.CharField(max_length=150, blank=True, null=True)
    aggregated_score_computed_value = models.FloatField(default=0, editable=False)
    slug = models.SlugField(unique=True, db_index=True, default=uuid.uuid4(), blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Evaluation Reports'

    def __str__(self):
        return f"{self.course.course_code} - {self.course.name}"

    def save(self, *args, **kwargs):
        slug_value = self.course.name + '-' + str(self.facilitator.staff_id)
        self.slug = slugify(slug_value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('evaluation', args=[self.slug])


class EvaluationSubmission(models.Model):
    evaluationInfo = models.ForeignKey(Evaluation, blank=True, null=True, on_delete=models.CASCADE,
                                       related_name='submitted_evaluations')

    curriculum_feedback_beginning_answer = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    curriculum_feedback_course_answer = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    curriculum_feedback_lecture_answer = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    curriculum_feedback_procedures_answer = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    curriculum_feedback_books_answer = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    curriculum_computed_value_answer = models.FloatField(default=0, editable=False)

    attendance_schedule = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    attendance_punctuality = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    attendance_presence = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)

    delivery_enthusiasm = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    delivery_sequence = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    delivery_organization = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    delivery_clarity = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    delivery_contents = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    delivery_responsiveness = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    delivery_achievements = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    delivery_innovation = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    delivery_theory_practices = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)

    assignments_relevance = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    assignments_promptitude = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    assignments_feedback = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    assignments_guidance = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)

    interaction_availability = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    interaction_help = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    interaction_fairness = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)

    environment_classroom_size = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    environment_seats = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    environment_audio_visual_equip = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    environment_public_address = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    environment_books = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    environment_computers = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    environment_internet = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    environment_air_conditioning = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)
    environment_secretariat = models.IntegerField(choices=FeedbackChoices.choices, blank=True, null=True)

    slug = models.SlugField(blank=True, null=True, unique=True, default=uuid.uuid4(), db_index=True)
    submitter = models.ForeignKey(Student, blank=True, null=True, on_delete=models.PROTECT)
    is_evaluated = models.BooleanField(blank=False, null=False, default=False)

    # deadline = models.DateTimeField(null=False,blank=False, default=datetime.datetime)

    def __str__(self):
        return f"{self.evaluationInfo} {self.submitter}"

    def save(self, *args, **kwargs):
        self.slug = str(self.evaluationInfo) + '-' + str(uuid.uuid4())
        self.slug = slugify(self.slug[50:])
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('evaluation', args=[self.slug])

    class Meta:
        unique_together = [('submitter', 'evaluationInfo')]


# Organisation Models
class Facilitator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_id = models.IntegerField(default=0)
    school = models.ForeignKey('School', on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + str(self.staff_id) + ")"


class School(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=250)
    school = models.ForeignKey('School', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    choices = (
        ('100', 'Level 100'),
        ('200', 'Level 200'),
        ('300', 'Level 300'),
        ('400', 'Level 400'),
        ('500', 'Level 500'),
        ('600', 'Level 600'),
    )

    name = models.CharField(max_length=250)
    course_code = models.CharField(max_length=10)
    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    level = models.CharField(default='', max_length=15, choices=choices)
    facilitator = models.ForeignKey('Facilitator', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.course_code + " (" + str(self.level) + ")"


# Signals
@receiver(post_save, sender=Evaluation)
def evaluation_created(sender, instance, created, *args, **kwargs):
    if created:
        EvaluationSubmission.objects.create(evaluationInfo=instance)
        print("Evaluation Submission form created successfully")
    else:
        print("Evaluation Submission form failed to create")
