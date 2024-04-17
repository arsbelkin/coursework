# Generated by Django 4.2.11 on 2024-04-16 18:37

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True, verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=users.models.user_directory_path,
                verbose_name="Фотография",
            ),
        ),
    ]
