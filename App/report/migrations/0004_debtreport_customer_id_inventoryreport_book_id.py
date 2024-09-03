# Generated by Django 5.0.6 on 2024-09-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("report", "0003_alter_debtreport_month_alter_inventoryreport_month"),
    ]

    operations = [
        migrations.AddField(
            model_name="debtreport",
            name="customer_id",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Customer ID"
            ),
        ),
        migrations.AddField(
            model_name="inventoryreport",
            name="book_id",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Book ID"
            ),
        ),
    ]