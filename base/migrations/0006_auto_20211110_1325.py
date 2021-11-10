# Generated by Django 3.2.9 on 2021-11-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_constructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='points',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
