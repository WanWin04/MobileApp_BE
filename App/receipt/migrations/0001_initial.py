# Generated by Django 5.0.6 on 2024-07-31 13:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Receipt",
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
                (
                    "customer_name",
                    models.CharField(max_length=250, verbose_name="Customer Name"),
                ),
                ("address", models.CharField(max_length=250, verbose_name="Address")),
                (
                    "phone_number",
                    models.CharField(max_length=20, verbose_name="Phone Number"),
                ),
                ("email", models.EmailField(max_length=250, verbose_name="Email")),
                ("payment_date", models.DateField(verbose_name="Payment Date")),
                (
                    "paid_amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Payment Amount"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]