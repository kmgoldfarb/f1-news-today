# Generated by Django 3.2.9 on 2021-11-11 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_race'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='link',
            field=models.CharField(default='formula1.com', max_length=500),
            preserve_default=False,
        ),
    ]
