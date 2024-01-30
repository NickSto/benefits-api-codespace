# Generated by Django 4.2.6 on 2024-01-30 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("translations", "0004_translation_no_auto"),
        ("programs", "0064_merge_20240126_1001"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="warning",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="program_warning",
                to="translations.translation",
            ),
        ),
        migrations.AddField(
            model_name="urgentneed",
            name="warning",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="urgent_need_warning",
                to="translations.translation",
            ),
        ),
    ]
