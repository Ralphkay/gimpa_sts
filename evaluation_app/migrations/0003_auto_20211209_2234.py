# Generated by Django 3.2.9 on 2021-12-09 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation_app', '0002_alter_evaluationsubmission_submitter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='evaluation',
        ),
        migrations.DeleteModel(
            name='Punctuality',
        ),
        migrations.DeleteModel(
            name='Curriculum',
        ),
    ]