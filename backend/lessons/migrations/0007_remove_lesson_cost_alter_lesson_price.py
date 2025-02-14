# Generated by Django 4.1.3 on 2022-12-03 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0006_lesson_deadline_datetime_lesson_link_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lesson",
            name="cost",
        ),
        migrations.AlterField(
            model_name="lesson",
            name="price",
            field=models.FloatField(
                validators=[django.core.validators.MinValueValidator(limit_value=0)]
            ),
        ),
    ]
