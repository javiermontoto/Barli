# Generated by Django 4.2.6 on 2024-01-12 01:41

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_bar_address_alter_bar_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='completed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_datetime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(validators=[api.models.UserProfile.validate_age]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fullname',
            field=models.CharField(max_length=255, validators=[api.models.UserProfile.validate_name]),
        ),
    ]
