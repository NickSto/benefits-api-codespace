# Generated by Django 4.0.5 on 2022-10-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0014_programtranslation_estimated_application_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='programtranslation',
            name='active',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]