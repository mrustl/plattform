# Generated by Django 3.1.5 on 2021-02-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ews', '0029_predictionmodel_fit'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictionmodel',
            name='predict',
            field=models.BooleanField(default=False),
        ),
    ]
