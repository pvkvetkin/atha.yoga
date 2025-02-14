# Generated by Django 4.1.4 on 2022-12-16 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("core", "0012_remove_questionnaireteacher_certificate_photo_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="questionnaireteachercertificatephoto",
            options={"base_manager_name": "objects"},
        ),
        migrations.AlterModelOptions(
            name="questionnaireteacherpassportphoto",
            options={"base_manager_name": "objects"},
        ),
        migrations.AlterModelOptions(
            name="questionnaireteacheruserphoto",
            options={"base_manager_name": "objects"},
        ),
        migrations.RemoveField(
            model_name="questionnaireteachercertificatephoto",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="questionnaireteachercertificatephoto",
            name="id",
        ),
        migrations.RemoveField(
            model_name="questionnaireteachercertificatephoto",
            name="image",
        ),
        migrations.RemoveField(
            model_name="questionnaireteachercertificatephoto",
            name="polymorphic_ctype",
        ),
        migrations.RemoveField(
            model_name="questionnaireteachercertificatephoto",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacherpassportphoto",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacherpassportphoto",
            name="id",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacherpassportphoto",
            name="image",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacherpassportphoto",
            name="polymorphic_ctype",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacherpassportphoto",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacheruserphoto",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacheruserphoto",
            name="id",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacheruserphoto",
            name="image",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacheruserphoto",
            name="polymorphic_ctype",
        ),
        migrations.RemoveField(
            model_name="questionnaireteacheruserphoto",
            name="updated_at",
        ),
        migrations.CreateModel(
            name="Attachment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
        ),
        migrations.AddField(
            model_name="questionnaireteachercertificatephoto",
            name="attachment_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="core.attachment",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="questionnaireteacherpassportphoto",
            name="attachment_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="core.attachment",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="questionnaireteacheruserphoto",
            name="attachment_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="core.attachment",
            ),
            preserve_default=False,
        ),
    ]
