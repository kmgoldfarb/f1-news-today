# Generated by Django 3.2.9 on 2021-11-11 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_rename_name_driver_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='last_name',
            new_name='name',
        ),
    ]
