# Generated by Django 4.1.7 on 2023-03-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="s_l",
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
                ("full_link", models.CharField(max_length=200)),
                ("short_link", models.CharField(max_length=6)),
            ],
        ),
    ]
