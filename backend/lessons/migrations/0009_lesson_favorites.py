# Generated by Django 4.1.4 on 2022-12-11 11:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lessons", "0008_alter_comment_options_alter_lesson_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="favorites",
            field=models.ManyToManyField(
                blank=True, related_name="favorite_lessons", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
