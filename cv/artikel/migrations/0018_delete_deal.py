# Generated by Django 3.1.2 on 2020-12-27 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0017_remove_deal_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Deal',
        ),
    ]
