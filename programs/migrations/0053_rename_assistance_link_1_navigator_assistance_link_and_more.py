# Generated by Django 4.0.5 on 2023-09-06 20:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0052_alter_navigator_assistance_link_1_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="navigator",
            old_name="assistance_link_1",
            new_name="assistance_link",
        ),
        migrations.RenameField(
            model_name="navigator",
            old_name="description_1",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="navigator",
            old_name="email_1",
            new_name="email",
        ),
        migrations.RenameField(
            model_name="navigator",
            old_name="name_1",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="urgentneed",
            old_name="description_1",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="urgentneed",
            old_name="link_1",
            new_name="link",
        ),
        migrations.RenameField(
            model_name="urgentneed",
            old_name="name_1",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="urgentneed",
            old_name="type_1",
            new_name="type",
        ),
    ]
