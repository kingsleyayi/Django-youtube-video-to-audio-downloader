# Generated by Django 3.0.2 on 2020-02-27 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp3', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Songs',
            new_name='Song',
        ),
    ]
