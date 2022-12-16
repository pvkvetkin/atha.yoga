# Generated by Django 4.1.4 on 2022-12-16 17:30
from django.apps.registry import Apps
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


def forwards_func(apps: Apps) -> None:
    MyModel = apps.get_model('lessons', 'Comment')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    new_ct = ContentType.objects.get_for_model(MyModel)
    MyModel.objects.filter(polymorphic_ctype__isnull=True).update(polymorphic_ctype=new_ct)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
        ("lessons", "0009_lesson_favorites"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="comment",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_%(app_label)s.%(class)s_set+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.RunPython(forwards_func, migrations.RunPython.noop)
    ]
