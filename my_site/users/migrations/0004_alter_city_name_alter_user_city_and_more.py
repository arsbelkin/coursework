# Generated by Django 4.2.11 on 2024-04-05 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_city_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="name",
            field=models.CharField(
                db_index=True, max_length=25, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.city",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(
                blank=True,
                default="01-01-2005",
                null=True,
                verbose_name="Дата рождения",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="users", verbose_name="Фотография"
            ),
        ),
    ]
