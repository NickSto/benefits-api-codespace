# Generated by Django 4.0.5 on 2023-06-01 22:11

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0038_program_fpl'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebHookFunction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Referrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referrer_code', models.CharField(max_length=64, unique=True)),
                ('webhook_url', models.CharField(blank=True, max_length=320, null=True)),
                ('logo', models.ImageField(upload_to='')),
                ('white_label_css', models.FileField(upload_to='')),
                ('primary_navigators', models.ManyToManyField(blank=True, related_name='primary_navigators', to='programs.navigator')),
                ('webhook_functions', models.ManyToManyField(blank=True, related_name='web_hook', to='programs.webhookfunction')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ReferrerTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('header_html', models.FileField(upload_to='')),
                ('footer_html', models.FileField(upload_to='')),
                ('consent_text', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='programs.referrer')),
            ],
            options={
                'verbose_name': 'referrer Translation',
                'db_table': 'programs_referrer_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
