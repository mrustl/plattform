# Generated by Django 3.1.5 on 2021-02-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ews', '0027_auto_20210128_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictionmodel',
            name='bathing_spot',
        ),
        migrations.AlterField(
            model_name='selectarea',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
