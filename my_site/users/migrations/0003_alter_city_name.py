# Generated by Django 4.2.11 on 2024-04-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_city_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="name",
            field=models.CharField(db_index=True, max_length=25, unique=True),
        ),
    ]
