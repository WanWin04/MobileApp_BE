# Generated by Django 5.0.6 on 2024-09-03 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_import_order", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="importbookorder",
            name="user_id",
        ),
        migrations.RemoveField(
            model_name="orderdetail",
            name="book",
        ),
        migrations.AddField(
            model_name="orderdetail",
            name="author",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="orderdetail",
            name="book_id",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="orderdetail",
            name="book_name",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="importbookorder",
            name="order_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="orderdetail",
            name="amount",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="orderdetail",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="details",
                to="book_import_order.importbookorder",
            ),
        ),
    ]
