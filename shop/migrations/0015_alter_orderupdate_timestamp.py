# Generated by Django 4.2.7 on 2023-11-19 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0014_alter_orderupdate_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderupdate",
            name="timestamp",
            field=models.DateTimeField(default="2023-11-19 13:55:23"),
        ),
    ]