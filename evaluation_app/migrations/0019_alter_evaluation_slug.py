# Generated by Django 4.0.1 on 2022-03-20 08:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation_app', '0018_alter_evaluation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
    ]