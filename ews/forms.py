from ews.models import BathingSpot, Station, FeatureData, FeatureType, PredictionModel
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit


class BathingSpotForm(forms.ModelForm):
    class Meta:
        model = BathingSpot
        fields=[ "name", "description"]
        widgets={"description": forms.Textarea(attrs={'rows':4})}


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields=["name", "feature_type", "bathing_spot"]


class FeatureDataForm(forms.ModelForm):
    class Meta:
        model = FeatureData
        fields=["date", "value", "station"]

class PredictionModelForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(PredictionModelForm, self).__init__(*args, **kwargs)
        self.fields['station'].help_text = "Please select the predictor variable which you want to use to model calibration"
        self.fields['station'].empty_label = None
        self.fields['bathing_spot'].empty_label = None
        self.fields['bathing_spot'].help_text = "Please select the bathing water for which you want to create a prediction model"
        self.fields['station'].queryset = Station.objects.filter(owner = user)
        self.fields['bathing_spot'].queryset = BathingSpot.objects.filter(user = user)
        
        self.helper = FormHelper()
    class Meta:
        model =  PredictionModel
        fields=["bathing_spot", "station"]
        widgets={"station": forms.CheckboxSelectMultiple()}