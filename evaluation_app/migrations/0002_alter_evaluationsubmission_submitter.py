# Generated by Django 3.2.9 on 2021-12-09 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
        ('evaluation_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.student'),
        ),
    ]
