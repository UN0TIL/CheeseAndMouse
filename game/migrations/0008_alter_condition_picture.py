# Generated by Django 5.1.4 on 2024-12-19 21:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_alter_condition_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='picture',
            field=models.ImageField(blank=True, default='condition/default.png', null=True, upload_to='condition/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions='png')]),
        ),
    ]
