# Generated by Django 4.1.7 on 2023-03-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0013_remove_doctor_orders_doctor_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="address",
            field=models.CharField(default="", max_length=255, verbose_name="地址"),
        ),
    ]