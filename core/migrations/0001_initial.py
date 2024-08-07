# Generated by Django 4.2.14 on 2024-07-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("full_name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
                ("is_read", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "İteşim",
                "verbose_name_plural": "İteşim",
            },
        ),
    ]
