# Generated by Django 4.0.1 on 2022-03-20 08:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation_app', '0012_alter_course_slug_alter_evaluation_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('9440f820-bafb-49f5-997a-0e643a295d5d'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('b9b5d320-9b7f-418a-bf2b-f5f3f87ed801'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('0f972149-7263-4898-af39-d760d585b434'), null=True, unique=True),
        ),
    ]
