# Generated by Django 3.1.5 on 2021-01-27 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ews', '0023_auto_20210124_1441'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='featuredata',
            unique_together={('date', 'site', 'value')},
        ),
    ]
