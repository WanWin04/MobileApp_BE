# Generated by Django 4.2.13 on 2024-09-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipt", "0007_alter_receipt_receipt_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipt",
            name="customer_id",
            field=models.CharField(
                max_length=10, null=True, verbose_name="Customer ID"
            ),
        ),
    ]
