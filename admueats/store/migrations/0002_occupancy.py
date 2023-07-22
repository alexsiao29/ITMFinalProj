# Generated by Django 4.2.3 on 2023-07-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Occupancy",
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
                ("table", models.CharField(max_length=50)),
                ("customer_email", models.EmailField(max_length=254)),
            ],
        ),
    ]