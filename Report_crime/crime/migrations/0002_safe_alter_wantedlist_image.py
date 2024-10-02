# Generated by Django 4.2.13 on 2024-09-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crime", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="safe",
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
                ("From", models.CharField(max_length=20)),
                ("precaution", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="wantedlist",
            name="image",
            field=models.ImageField(upload_to="static/"),
        ),
    ]
