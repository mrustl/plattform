from import_export import resources, fields
from .models import  Site, BathingSpot, FeatureData
from import_export.widgets import ForeignKeyWidget
#from django.contrib.auth.models import User


class FeatureDataResource(resources.ModelResource):

    site_id = fields.Field(
        column_name='site_id',
        attribute='site_id',
        widget=ForeignKeyWidget(Site, 'Site'))

#

    class Meta:
        model = FeatureData