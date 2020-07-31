from import_export import resources, fields
from .models import  Station, BathingSpot, FeatureData
from import_export.widgets import ForeignKeyWidget
#from django.contrib.auth.models import User


class FeatureDataResource(resources.ModelResource):

    station_id = fields.Field(
        column_name='station_id',
        attribute='station_id',
        widget=ForeignKeyWidget(Station, 'Station'))

#

    class Meta:
        model = FeatureData