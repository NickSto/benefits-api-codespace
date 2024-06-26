# Generated by Django 4.2.6 on 2024-01-30 18:46

from django.db import migrations


def add_warning(apps, schema_editor):
    Program = apps.get_model("programs", "Program")
    UrgentNeed = apps.get_model("programs", "UrgentNeed")
    Translation = apps.get_model("translations", "Translation")

    for need in UrgentNeed.objects.all():
        translation = Translation.objects.add_translation(f"urgent_need.{need.name.text}-{need.id}_warning", "")
        UrgentNeed.objects.filter(pk=need.id).update(warning=translation.id)

    for program in Program.objects.all():
        translation = Translation.objects.add_translation(
            f"programs.{program.name_abbreviated}-{program.id}_warning", ""
        )
        Program.objects.filter(pk=program.id).update(warning=translation.id)


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0065_program_warning_urgentneed_warning"),
        ("translations", "0004_translation_no_auto"),
    ]

    operations = [migrations.RunPython(add_warning)]
