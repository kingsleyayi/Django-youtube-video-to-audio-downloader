# Generated by Django 3.0.2 on 2020-03-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp3', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
