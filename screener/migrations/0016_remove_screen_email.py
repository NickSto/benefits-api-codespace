# Generated by Django 4.0.5 on 2022-08-10 17:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0015_remove_screen_cell"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="screen",
            name="email",
        ),
    ]
