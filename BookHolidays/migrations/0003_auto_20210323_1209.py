# Generated by Django 3.1.7 on 2021-03-23 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BookHolidays', '0002_auto_20210323_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='accounts',
        ),
        migrations.AddField(
            model_name='staff',
            name='first_name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
