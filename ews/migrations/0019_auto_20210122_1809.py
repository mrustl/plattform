# Generated by Django 3.1.5 on 2021-01-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ews', '0018_auto_20210121_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuretype',
            name='unit',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
