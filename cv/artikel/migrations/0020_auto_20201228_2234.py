# Generated by Django 3.1.2 on 2020-12-28 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0019_auto_20201228_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikelmodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=6, null=True, unique=True),
        ),
    ]
