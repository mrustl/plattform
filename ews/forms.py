from ews.models import BathingSpot, Station, FeatureData, FeatureType
from django.forms import ModelForm


class BathingSpotForm(ModelForm):
    class Meta:
        model = BathingSpot
        fields=[ "name"]


class StationForm(ModelForm):
    class Meta:
        model = Station
        fields=["name", "feature_type", "bathing_spot"]


class FeatureDataForm(ModelForm):
    class Meta:
        model = FeatureData
        fields=["date", "value", "station"]