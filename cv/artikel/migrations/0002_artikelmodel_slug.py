# Generated by Django 3.1.2 on 2020-11-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikelmodel',
            name='slug',
            field=models.SlugField(max_length=12, null=True),
        ),
    ]
