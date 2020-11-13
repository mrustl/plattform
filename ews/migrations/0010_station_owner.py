# Generated by Django 3.0.8 on 2020-08-06 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ews', '0009_bathingspot_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
