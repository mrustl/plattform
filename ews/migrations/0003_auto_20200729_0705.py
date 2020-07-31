# Generated by Django 3.0.8 on 2020-07-29 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ews', '0002_featuredata'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('unit', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('PredictorType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictor_type', to='ews.FeatureType')),
                ('bathing_spot', models.ManyToManyField(blank=True, related_name='rainstations', to='ews.BathingSpot')),
            ],
        ),
        migrations.AlterField(
            model_name='featuredata',
            name='rainstation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station', to='ews.Station'),
        ),
        migrations.DeleteModel(
            name='RainStation',
        ),
    ]