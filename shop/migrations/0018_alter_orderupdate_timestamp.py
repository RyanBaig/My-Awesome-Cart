# Generated by Django 4.0.6 on 2023-11-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_orderupdate_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(default='2023-11-20 21:32:48'),
        ),
    ]
