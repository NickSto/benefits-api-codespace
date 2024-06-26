# Generated by Django 4.2.11 on 2024-05-21 20:55
import uuid
from django.db import migrations


def add_estimated_value(apps, schema_editor):
    UrgentNeed = apps.get_model("programs", "UrgentNeed")
    Translation = apps.get_model("translations", "Translation")

    for urgent_need in UrgentNeed.objects.all():
        translation = Translation.objects.add_translation(
            f"urgent_need.{urgent_need.external_name or uuid.uuid4()}-{urgent_need.id}_website_description",
            "[PLACEHOLDER]",
        )
        UrgentNeed.objects.filter(pk=urgent_need.id).update(website_description=translation.id)


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0075_urgentneed_website_description"),
        ("translations", "0004_translation_no_auto"),
    ]

    operations = [migrations.RunPython(add_estimated_value, migrations.RunPython.noop)]
