# Generated by Django 4.2.13 on 2024-09-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_import_order", "0002_remove_importbookorder_user_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="importbookorder",
            name="amount",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="importbookorder",
            name="author",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="importbookorder",
            name="book_id",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="importbookorder",
            name="book_name",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name="OrderDetail",
        ),
    ]
