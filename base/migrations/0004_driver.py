# Generated by Django 3.2.9 on 2021-11-10 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_article_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=10)),
                ('team', models.CharField(max_length=100)),
            ],
        ),
    ]
