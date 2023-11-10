# Generated by Django 4.2.5 on 2023-11-10 00:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blogpost",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("head0", models.CharField(default="", max_length=500)),
                ("head1", models.CharField(default="", max_length=500)),
                ("head2", models.CharField(default="", max_length=500)),
                ("pub_date", models.DateField()),
                ("thumbnail", models.ImageField(default="", upload_to="blog/images")),
            ],
        ),
    ]
