# Generated by Django 5.0.6 on 2024-08-31 07:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("report", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DebtReport",
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
                ("month", models.DateField(verbose_name="Date")),
                (
                    "customer_name",
                    models.CharField(max_length=250, verbose_name="Customer Name"),
                ),
                ("begin", models.IntegerField(verbose_name="Begin")),
                ("arise", models.IntegerField(verbose_name="Arise")),
                ("end", models.IntegerField(verbose_name="End")),
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
            name="InventoryReport",
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
                ("month", models.DateField(verbose_name="Date")),
                (
                    "book_name",
                    models.CharField(max_length=250, verbose_name="Book Name"),
                ),
                ("begin", models.IntegerField(verbose_name="Begin")),
                ("arise", models.IntegerField(verbose_name="Arise")),
                ("end", models.IntegerField(verbose_name="End")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Report",
        ),
    ]