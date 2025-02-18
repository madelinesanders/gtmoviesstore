# Generated by Django 5.1.4 on 2025-02-16 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_movie_id_alter_movie_imageurl"),
        ("shopping_cart", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.movie"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shopping_cart.order",
                    ),
                ),
            ],
        ),
    ]
