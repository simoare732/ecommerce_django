# Generated by Django 5.1.1 on 2024-12-08 17:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_rename_user_question_reg_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'user')},
        ),
    ]
