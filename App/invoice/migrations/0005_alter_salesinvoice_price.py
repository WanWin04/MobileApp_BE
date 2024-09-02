# Generated by Django 4.2.13 on 2024-09-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0004_remove_salesinvoice_customer_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salesinvoice",
            name="price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="Price",
            ),
        ),
    ]
