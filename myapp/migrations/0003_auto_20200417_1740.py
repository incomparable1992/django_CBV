# Generated by Django 3.0.5 on 2020-04-17 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_notes_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'managed': True, 'verbose_name_plural': 'NOTE'},
        ),
    ]
