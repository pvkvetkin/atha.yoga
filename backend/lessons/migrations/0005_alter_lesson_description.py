# Generated by Django 4.1.3 on 2022-12-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0004_lesson_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
