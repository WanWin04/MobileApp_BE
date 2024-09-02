# Generated by Django 5.0.6 on 2024-09-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipt", "0005_remove_receipt_id_alter_receipt_receipt_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="paid_amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Payment Amount"
            ),
        ),
    ]
