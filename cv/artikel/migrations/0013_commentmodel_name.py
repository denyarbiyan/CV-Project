# Generated by Django 3.1.2 on 2020-12-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0012_auto_20201209_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
