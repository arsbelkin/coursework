# Generated by Django 4.2.11 on 2024-04-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_city_name_alter_user_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(
                blank=True,
                default="2005-01-01",
                null=True,
                verbose_name="Дата рождения",
            ),
        ),
    ]
