# Generated by Django 3.2.7 on 2023-08-23 22:22

from django.db import migrations


def populate_languages(apps, schema_editor):
    Language = apps.get_model('base', 'Language')

    with open('langs_list.py', 'r', encoding='utf-8') as file:
        for line in file:
            name_english, name_native = line.strip().split(' - ')
            Language.objects.create(name_english=name_english, name_native=name_native)


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20230823_1619'),
    ]

    operations = [
        migrations.RunPython(populate_languages),
    ]
