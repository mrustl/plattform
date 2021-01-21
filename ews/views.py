from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BathingSpotForm, StationForm, FeatureDataForm, PredictionModelForm, PredictionModelForm2
from .models import BathingSpot, Station, FeatureData, FeatureType, User, PredictionModel
from django.urls import reverse
from tablib import Dataset, core
from .resources import FeatureDataResource
from django.contrib.auth.decorators import login_required
import numpy as np
import pandas as  pd
from django.db import IntegrityError
import plotly.express as px
from plotly.offline import plot
from django_pandas.io import read_frame
# Create your views here.

@login_required
def bathingspots(request):
    entries = BathingSpot.objects.filter(user = request.user)

    return render(request, "ews/index.html", {"entries": entries})

@login_required
def stations(request):
    stations = Station.objects.filter(owner = request.user)
    return render(request, "ews/stations.html", {"entries": stations,"item": "spot"})

@login_required(login_url="login")
def mlmodels(request):
    mlmodels = PredictionModel.objects.filter(user = request.user)
    return render(request, "ews/models.html", {"entries": mlmodels})

@login_required
def model_config(request):
    if request.method == "POST":
        form = PredictionModelForm(request.user, request.POST)
        if form.is_valid():
            pmodel = PredictionModel()
            pmodel.user = request.user
            pmodel.name = form.cleaned_data["name"]
            pmodel.bathing_spot=form.cleaned_data["bathing_spot"]
            pmodel.save()
            pmodel.station.set(form.cleaned_data["station"])
            pmodel.save()
            return HttpResponseRedirect(reverse("ews:mlmodels"))
        else:
            return HttpResponse(request, "Form not valid")

        return HttpResponseRedirect(reverse("ews:mlmodels"))
    else:
        pmodel_form = PredictionModelForm(request.user)
        return render(request, "ews/model_config.html", {"pmodel_form": pmodel_form})


@login_required
def model_config2(request):
    if request.method == "POST":
        form = PredictionModelForm2(request.user, request.POST)
        if form.is_valid():
            pmodel = PredictionModel()
            pmodel.user = request.user
            pmodel.name = form.cleaned_data["name"]
            pmodel.bathing_spot=form.cleaned_data["bathing_spot"]
            pmodel.save()
            pmodel.station.set(form.cleaned_data["flow_station"])
            pmodel.save()
           
            
            return HttpResponseRedirect(reverse("ews:mlmodels"))
        else:
            return HttpResponse(request, "Form not valid")

        return HttpResponseRedirect(reverse("ews:mlmodels"))
    else:
  
        pmodel_form2 = PredictionModelForm2(request.user)
        return render(request, "ews/model_config.html", { "pmodel_form2":pmodel_form2})








@login_required
def spot_create(request):
    if request.method == "POST":
        form = BathingSpotForm(request.POST)
        user = request.user
        if form.is_valid():
            spot = BathingSpot()
            spot.name = form.cleaned_data["name"]
            spot.description = form.cleaned_data["description"]
            spot.user = user
            spot.save()
        return HttpResponseRedirect(reverse('ews:bathing_spots'))
    else:
        form = BathingSpotForm()          
    return render(request, "ews/create.html", {"form":form})




@login_required
def detail_view(request, spot_id):
    entries = BathingSpot.objects.get(id = spot_id)
    stations = entries.stations.values()
    #featuretype = []
    
    for i in range(len(stations)):
        stations[i]["feature_type"] = FeatureType.objects.get(id = stations[i]['feature_type_id'])
    
    return render(request, "ews/detail.html", {"entries": entries, "stations":stations})


@login_required
def add_station(request):
    new_station = Station()
    if request.method == "POST":
        form = StationForm(request.POST)
       # form.owner=request.user
        if form.is_valid():
            
            new_station.name=form.cleaned_data["name"]
            new_station.feature_type=form.cleaned_data["feature_type"]
            
            new_station.owner=request.user
            new_station.save()
            new_station.bathing_spot.set(form.cleaned_data["bathing_spot"])
            new_station.save()

        return HttpResponseRedirect(reverse('ews:stations'))
    else:
        # prepopulating with dictionary
        form = StationForm()
        user_id = User.objects.filter(username=request.user).values()[0]["id"]
        spot= BathingSpot.objects.filter(user = user_id) 
    return render(request, "ews/add_station.html", {"form":form, "spot":spot})

def delete_station(request, station_id):
    Station.objects.get(id=station_id).delete()
    return HttpResponseRedirect(reverse('ews:stations'))

def delete_model(request, model_id):
    PredictionModel.objects.get(id=model_id).delete()
    return HttpResponseRedirect(reverse('ews:mlmodels'))




@login_required
def add_data(request):
    if request.method == "POST":
        form = FeatureDataForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('ews:add_station'))
    else:
        form = FeatureDataForm()
        
    return render(request, "ews/add_data.html", {"form":form})

#def delete_station(request, station_id):
#    Station.objects.filter(id=station_id).delete()
 #   return render(request, )

#@login_required
@login_required
def file_upload(request, station_id):
    if request.method == 'POST':

        feature_resource = FeatureDataResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']


        imported_data = dataset.load(new_data.read().decode("utf-8"), format="csv")
        #create an array containing the location_id
        location_arr = [station_id] * len(imported_data)

        # use the tablib API to add a new column, and insert the location array values
        imported_data.append_col(location_arr, header="station")

        try:
            result = feature_resource.import_data(dataset, dry_run=True)  # Test the data import
        except Exception as e:
            return HttpResponse(e, status=status.HTTP_400_BAD_REQUEST)

        if not result.has_errors():
            feature_resource.import_data(dataset, dry_run=False)  # Actually import now
        
        return HttpResponseRedirect(reverse("ews:station_detail",    args=[station_id,]))
    return render(request, 'ews/import.html', {"station_id":station_id})



def station_detail(request, station_id):
        df = read_frame(FeatureData.objects.filter(station_id=station_id))
        fig = px.bar(df, "date", "value")
        fig = plot(fig, output_type = "div")
        return render(request, "ews/station_detail.html", {"fig":fig, "data":df.to_html()})
    





def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "ews/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "ews/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("ews:mlmodels"))
    else:
        return render(request, "ews/register.html")

