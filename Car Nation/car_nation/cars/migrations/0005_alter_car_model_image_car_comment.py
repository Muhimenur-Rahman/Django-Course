# Generated by Django 5.0.7 on 2024-09-21 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0004_car_model_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car_model",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="cars/media/uploads/"
            ),
        ),
        migrations.CreateModel(
            name="car_comment",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("body", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="cars.car_model",
                    ),
                ),
            ],
        ),
    ]
