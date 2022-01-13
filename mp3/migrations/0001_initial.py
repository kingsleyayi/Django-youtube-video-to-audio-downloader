# Generated by Django 3.0.2 on 2020-02-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('year', models.CharField(max_length=200, null=True)),
                ('artist', models.CharField(max_length=200, null=True)),
                ('genre', models.CharField(choices=[('afro', 'afro'), ('trap', 'trap')], max_length=200, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to='')),
                ('country', models.CharField(choices=[('naija', 'naija'), ('us', 'us'), ('uk', 'uk'), ('SA', 'SA')], max_length=200, null=True)),
                ('album', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
