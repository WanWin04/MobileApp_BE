# Generated by Django 5.0.6 on 2024-09-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0005_alter_salesinvoice_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesinvoice",
            name="book_id",
            field=models.CharField(max_length=10, null=True, verbose_name="Book ID"),
        ),
    ]
