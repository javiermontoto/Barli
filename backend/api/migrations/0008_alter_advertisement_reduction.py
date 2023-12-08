# Generated by Django 4.2.6 on 2023-12-02 16:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_advertisement_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='reduction',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(95)]),
        ),
    ]
