# Generated by Django 5.1.5 on 2025-02-18 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
