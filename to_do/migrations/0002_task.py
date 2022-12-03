# Generated by Django 4.1.2 on 2022-11-30 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("to_do", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("content", models.TextField(max_length=255)),
                ("create", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField(blank=True)),
                ("done_or_not", models.BooleanField(default=False)),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="tags", to="to_do.tag"
                    ),
                ),
            ],
            options={
                "ordering": ["done_or_not", "create"],
            },
        ),
    ]