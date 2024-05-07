# Generated by Django 4.0.5 on 2022-12-08 22:13

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0016_alter_programtranslation_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Navigator",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="NavigatorTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("language_code", models.CharField(db_index=True, max_length=15, verbose_name="Language")),
                ("name", models.CharField(max_length=120)),
                (
                    "cell",
                    phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True, verbose_name="email address")),
                ("assistance_link", models.CharField(blank=True, max_length=320)),
                ("description", models.TextField()),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="programs.navigator",
                    ),
                ),
                ("program", models.ManyToManyField(to="programs.program")),
            ],
            options={
                "verbose_name": "navigator Translation",
                "db_table": "programs_navigator_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
