# Generated by Django 4.0.5 on 2023-05-09 20:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0035_federalpoverylimit"),
    ]

    operations = [
        migrations.RenameField(
            model_name="federalpoverylimit",
            old_name="has_2_person",
            new_name="has_2_people",
        ),
        migrations.RenameField(
            model_name="federalpoverylimit",
            old_name="has_3_person",
            new_name="has_3_people",
        ),
        migrations.RenameField(
            model_name="federalpoverylimit",
            old_name="has_4_person",
            new_name="has_4_people",
        ),
        migrations.RenameField(
            model_name="federalpoverylimit",
            old_name="has_5_person",
            new_name="has_5_people",
        ),
        migrations.RenameField(
            model_name="federalpoverylimit",
            old_name="has_6_person",
            new_name="has_6_people",
        ),
        migrations.RenameField(
            model_name="federalpoverylimit",
            old_name="has_7_person",
            new_name="has_7_people",
        ),
        migrations.RenameField(
            model_name="federalpoverylimit",
            old_name="has_8_person",
            new_name="has_8_people",
        ),
    ]
