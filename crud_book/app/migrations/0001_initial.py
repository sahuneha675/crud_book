# Generated by Django 4.1.5 on 2023-02-06 15:48

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=200)),
                ("isbn", models.PositiveIntegerField()),
                ("category", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="IssuedBook",
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
                ("student_id", models.CharField(blank=True, max_length=100)),
                ("isbn", models.CharField(max_length=13)),
                ("issued_date", models.DateField(auto_now=True)),
                ("expiry_date", models.DateField(default=app.models.expiry)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=200)),
                ("roll_no", models.CharField(max_length=200)),
                ("dob", models.DateField()),
                ("gender", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=250)),
                ("password", models.CharField(max_length=250)),
                ("phone", models.CharField(max_length=10)),
                ("subject", models.IntegerField()),
                ("image", models.ImageField(blank=True, upload_to="profile/")),
            ],
        ),
    ]