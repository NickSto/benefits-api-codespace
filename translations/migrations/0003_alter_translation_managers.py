# Generated by Django 4.0.5 on 2023-09-05 22:43

from django.db import migrations
import translations.models


class Migration(migrations.Migration):
    dependencies = [
        ("translations", "0002_translation_active"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="translation",
            managers=[
                ("objects", translations.models.TranslationManager()),
            ],
        ),
    ]
