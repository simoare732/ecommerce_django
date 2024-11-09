# Generated by Django 5.1.1 on 2024-11-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_strike_seen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strike',
            name='seen',
        ),
        migrations.AddField(
            model_name='report',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]