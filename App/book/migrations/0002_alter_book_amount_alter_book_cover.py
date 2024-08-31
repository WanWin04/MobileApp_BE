# Generated by Django 4.2.13 on 2024-08-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="amount",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="cover",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
