# Generated by Django 4.2.5 on 2023-11-10 00:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="chead0",
            field=models.CharField(default="", max_length=500),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="chead1",
            field=models.CharField(default="", max_length=500),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="chead2",
            field=models.CharField(default="", max_length=500),
        ),
    ]