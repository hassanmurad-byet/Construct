# Generated by Django 5.0.3 on 2024-05-18 16:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0003_rename_image_aboutinfo_about_image_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="homeinfo",
        ),
        migrations.DeleteModel(
            name="portfo",
        ),
    ]
