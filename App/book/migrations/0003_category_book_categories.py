# Generated by Django 4.2.13 on 2024-08-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0002_alter_book_amount_alter_book_cover"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cat_id", models.CharField(max_length=10, unique=True)),
                ("cat_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="categories",
            field=models.ManyToManyField(to="book.category"),
        ),
    ]
