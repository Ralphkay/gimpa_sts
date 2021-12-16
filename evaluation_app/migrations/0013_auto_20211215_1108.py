# Generated by Django 3.2.9 on 2021-12-15 11:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation_app', '0012_auto_20211215_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('d042bf1b-edbc-4656-b666-2c5bec8be603'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='is_evaluated',
            field=models.BooleanField(choices=[('True', True), ('False', False)], default=False),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('091d5682-63a0-4246-81b1-ed77f4ed9983'), null=True, unique=True),
        ),
    ]
