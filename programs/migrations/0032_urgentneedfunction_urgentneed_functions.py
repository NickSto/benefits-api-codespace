# Generated by Django 4.0.5 on 2023-03-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0031_urgentneed_urgentneedtranslation"),
    ]

    operations = [
        migrations.CreateModel(
            name="UrgentNeedFunction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name="urgentneed",
            name="functions",
            field=models.ManyToManyField(related_name="function", to="programs.urgentneedfunction"),
        ),
    ]
