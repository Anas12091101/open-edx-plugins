# Generated by Django 2.2.20 on 2021-05-04 09:00

import jsonfield.encoder
import jsonfield.fields
import opaque_keys.edx.django.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []  # type: ignore  # noqa: PGH003

    operations = [
        migrations.CreateModel(
            name="CourseGitLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course_id",
                    opaque_keys.edx.django.models.CourseKeyField(
                        db_index=True, max_length=255
                    ),
                ),
                (
                    "course_import_log",
                    jsonfield.fields.JSONField(
                        blank=True,
                        dump_kwargs={
                            "cls": jsonfield.encoder.JSONEncoder,
                            "separators": (",", ":"),
                        },
                        load_kwargs={},
                        null=True,
                    ),
                ),
                ("git_log", models.TextField(blank=True, null=True)),
                ("repo_dir", models.CharField(max_length=255)),
                ("commit", models.CharField(max_length=40, null=True)),
                ("author", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
