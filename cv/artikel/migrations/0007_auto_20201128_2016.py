# Generated by Django 3.1.2 on 2020-11-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0006_auto_20201128_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikelmodel',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
