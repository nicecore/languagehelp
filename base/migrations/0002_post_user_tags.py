# Generated by Django 3.2.7 on 2023-08-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_tags',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
