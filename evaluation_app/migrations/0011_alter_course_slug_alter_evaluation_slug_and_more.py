# Generated by Django 4.0.1 on 2022-03-20 08:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation_app', '0010_alter_course_slug_alter_evaluation_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('2bdb6844-45f6-4587-9d00-ceeb1e2a889d'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('6e6203cd-61db-43c4-a880-29ac98288cfe'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('8a494e41-e430-4ae5-9632-4b5cef84d292'), null=True, unique=True),
        ),
    ]
