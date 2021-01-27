from ews.models import BathingSpot, Site, FeatureData, FeatureType, PredictionModel
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit


class BathingSpotForm(forms.ModelForm):
    class Meta:
        model = BathingSpot
        fields=[ "name", "description"]
        widgets={"description": forms.Textarea(attrs={'rows':4})}


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields=["name", "feature_type"]


class FeatureDataForm(forms.ModelForm):
    class Meta:
        model = FeatureData
        fields=["date", "value", "site"]

class PredictionModelForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(PredictionModelForm, self).__init__(*args, **kwargs)
        self.fields['site'].help_text = "Please select the predictor variable which you want to use to model calibration"
        self.fields['site'].empty_label = None
        self.fields['bathing_spot'].empty_label = None
        self.fields['bathing_spot'].help_text = "Please select the bathing water for which you want to create a prediction model"
        self.fields['site'].queryset = Site.objects.filter(owner = user)
        self.fields['bathing_spot'].queryset = BathingSpot.objects.filter(user = user)
        
        self.helper = FormHelper()
    class Meta:
        model =  PredictionModel
        fields=["bathing_spot", "site", "site","name"]
        widgets={"site": forms.CheckboxSelectMultiple()}




class PredictionModelForm2(forms.Form):
    name=forms.CharField(label="Enter a informative name")
    bathing_spot=forms.ModelChoiceField(queryset= BathingSpot.objects.all())
    rain_site = forms.ModelMultipleChoiceField(queryset=Site.objects.all())
    flow_site = forms.ModelMultipleChoiceField(queryset=Site.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(PredictionModelForm2, self).__init__(*args, **kwargs)
        self.fields['rain_site'].queryset = Site.objects.filter(owner = user, feature_type = 1)
        self.fields['flow_site'].queryset = Site.objects.filter(owner = user, feature_type = 4)
        self.fields['bathing_spot'].queryset = BathingSpot.objects.filter(user = user)
        self.helper = FormHelper()

from leaflet.forms.widgets import LeafletWidget
from .models import SelectArea

class SelectAreaForm(forms.ModelForm):

    class Meta:
        model = SelectArea
        fields = ('name', 'geom', 'feature_type')
        widgets = {'geom': LeafletWidget()}


