# Generated by Django 2.2.5 on 2020-12-29 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20201228_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='county',
            new_name='country',
        ),
    ]
