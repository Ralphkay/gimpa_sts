# Generated by Django 4.0.1 on 2022-03-20 00:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation_app', '0007_alter_evaluation_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('a93c990f-b70f-41ce-a38e-381d9d3389e7'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('3891735e-439f-49a1-9106-4d57afb02445'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('aff94773-d21e-4333-aee4-c33f8379057c'), null=True, unique=True),
        ),
    ]
