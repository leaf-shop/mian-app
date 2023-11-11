# Generated by Django 4.2.7 on 2023-11-11 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("descriptions", models.TextField()),
                (
                    "score",
                    models.CharField(
                        choices=[
                            ("1", "Very Bad"),
                            ("2", "Bad"),
                            ("3", "Normal"),
                            ("4", "Good"),
                            ("5", "Great"),
                        ],
                        max_length=1,
                    ),
                ),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("demonstrable", models.BooleanField(default=True)),
                ("recommendable", models.BooleanField(default=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(db_index=True, max_length=50)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="share_module.category",
                    ),
                ),
            ],
        ),
    ]
