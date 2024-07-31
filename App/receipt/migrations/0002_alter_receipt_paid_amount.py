# Generated by Django 5.0.6 on 2024-07-31 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipt", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="paid_amount",
            field=models.DecimalField(
                decimal_places=0, max_digits=10, verbose_name="Payment Amount"
            ),
        ),
    ]
