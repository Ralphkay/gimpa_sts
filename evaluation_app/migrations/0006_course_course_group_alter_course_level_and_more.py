# Generated by Django 4.0.1 on 2022-03-19 11:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation_app', '0005_alter_evaluation_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_group',
            field=models.CharField(choices=[('day', 'Day'), ('evening', 'Evening'), ('weekend', 'Weekend')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('100', 'Level 100'), ('200', 'Level 200'), ('300', 'Level 300'), ('400', 'Level 400'), ('500', 'Level 500'), ('600', 'Level 600'), ('700', 'Level 700'), ('800', 'Level 800')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('70fcf972-1235-4736-b9f7-91e6b3fa9c16'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('daa8449b-4753-444a-819e-9cb6f9309f02'), null=True, unique=True),
        ),
    ]
