# Generated by Django 4.2.13 on 2024-09-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0003_alter_salesinvoice_customer_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="salesinvoice",
            name="customer_name",
        ),
        migrations.AddField(
            model_name="salesinvoice",
            name="customer_id",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Customer ID"
            ),
        ),
    ]
