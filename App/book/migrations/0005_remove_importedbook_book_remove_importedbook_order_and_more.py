# Generated by Django 4.2.13 on 2024-08-18 13:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0004_importbookorder_importedbook"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="importedbook",
            name="book",
        ),
        migrations.RemoveField(
            model_name="importedbook",
            name="order",
        ),
        migrations.DeleteModel(
            name="ImportBookOrder",
        ),
        migrations.DeleteModel(
            name="ImportedBook",
        ),
    ]
