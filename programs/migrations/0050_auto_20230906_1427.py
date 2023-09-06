# Generated by Django 4.0.5 on 2023-09-06 20:27

from django.db import migrations
from django.conf import settings


def urgent_need_migrations(apps, _):
    UrgentNeed = apps.get_model('programs', 'UrgentNeed')
    Translation = apps.get_model('translations', 'Translation')

    translated_fields = (
        'name',
        'description',
        'link',
        'type',
    )
    for urgent_need in UrgentNeed.objects.all():
        main_name = urgent_need.name
        for field in translated_fields:
            translation = Translation.objects.add_translation(f'urgent_need.{main_name}_{urgent_need.id}-{field}', getattr(urgent_need, field))
            setattr(urgent_need, field + '_1', translation)
            for lang in settings.PARLER_LANGUAGES[None]:
                urgent_need.set_current_language(lang['code'])
                Translation.objects.edit_translation(f'urgent_need.{main_name}_{urgent_need.id}-{field}', lang['code'], getattr(urgent_need, field), True)
        urgent_need.save()


def navigator_migrations(apps, _):
    Navigator = apps.get_model('programs', 'Navigator')
    Translation = apps.get_model('translations', 'Translation')

    translated_fields = (
        'name',
        'email',
        'assistance_link',
        'description',
    )
    for navigator in Navigator.objects.all():
        main_name = navigator.name
        for field in translated_fields:
            translation = Translation.objects.add_translation(f'navigator.{main_name}_{navigator.id}-{field}', getattr(navigator, field))
            setattr(navigator, field + '_1', translation)
            for lang in settings.PARLER_LANGUAGES[None]:
                navigator.set_current_language(lang['code'])
                Translation.objects.edit_translation(f'navigator.{main_name}_{navigator.id}-{field}', lang['code'], getattr(navigator, field), True)
        navigator.save()


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0049_navigator_assistance_link_1_navigator_description_1_and_more'),
        ('translations', '0003_alter_translation_managers'),
    ]

    operations = [
        migrations.RunPython(urgent_need_migrations),
        migrations.RunPython(navigator_migrations),
    ]
