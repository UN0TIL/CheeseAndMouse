# Generated by Django 5.1.4 on 2025-01-02 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_tasks_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='label',
        ),
    ]
