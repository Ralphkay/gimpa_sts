# Generated by Django 4.0.1 on 2022-03-20 08:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation_app', '0015_alter_course_slug_alter_evaluation_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('80256bad-35c3-4d3f-94e1-68b371072264'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('83163bca-8d09-4ca0-8c4a-5fb0b4f12c78'), null=True, unique=True),
        ),
    ]