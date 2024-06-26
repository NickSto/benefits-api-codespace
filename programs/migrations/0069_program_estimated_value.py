# Generated by Django 4.2.11 on 2024-05-06 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("translations", "0004_translation_no_auto"),
        ("programs", "0068_merge_20240130_1319"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="estimated_value",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="program_estimated_value",
                to="translations.translation",
            ),
        ),
    ]
