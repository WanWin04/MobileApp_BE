# Generated by Django 5.0.6 on 2024-08-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipt", "0002_alter_receipt_paid_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipt",
            name="receipt_id",
            field=models.CharField(default=0, max_length=10, verbose_name="Receipt ID"),
        ),
    ]
