# Generated by Django 5.0.6 on 2024-09-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driveruser",
            name="name",
            field=models.CharField(max_length=250, verbose_name="User Name"),
        ),
    ]
