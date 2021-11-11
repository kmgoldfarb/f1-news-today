# Generated by Django 3.2.9 on 2021-11-11 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20211110_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('flag', models.CharField(max_length=500)),
                ('track_img', models.CharField(max_length=500)),
            ],
        ),
    ]
