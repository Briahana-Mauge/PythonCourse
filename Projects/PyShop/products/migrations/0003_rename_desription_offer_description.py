# Generated by Django 5.0.7 on 2024-08-06 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_offer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="offer",
            old_name="desription",
            new_name="description",
        ),
    ]