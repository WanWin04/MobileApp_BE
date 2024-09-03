# Generated by Django 5.0.6 on 2024-09-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0006_salesinvoice_book_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesinvoice",
            name="customer_name",
            field=models.CharField(
                max_length=250, null=True, verbose_name="Customer Name"
            ),
        ),
    ]