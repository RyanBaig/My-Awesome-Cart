# Generated by Django 4.2.7 on 2023-11-17 23:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0013_alter_orderupdate_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderupdate",
            name="timestamp",
            field=models.DateTimeField(default="2023-11-18 04:14:25"),
        ),
    ]