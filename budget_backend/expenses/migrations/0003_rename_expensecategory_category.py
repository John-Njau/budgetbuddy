# Generated by Django 4.1.2 on 2022-10-23 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0002_author_article"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ExpenseCategory",
            new_name="Category",
        ),
    ]
