# Generated by Django 4.1.2 on 2022-10-23 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("budget", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Expense",
        ),
    ]
