from ews.models import BathingSpot, Station, FeatureData, FeatureType, PredictionModel
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit


class BathingSpotForm(forms.ModelForm):
    class Meta:
        model = BathingSpot
        fields=[ "name"]


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields=["name", "feature_type", "bathing_spot"]


class FeatureDataForm(forms.ModelForm):
    class Meta:
        model = FeatureData
        fields=["date", "value", "station"]

class PredictionModelForm(forms.ModelForm):
    class Meta:
        model =  PredictionModel
        fields=["bathing_spot", "station"]
        widgets={"station": forms.CheckboxSelectMultiple()}