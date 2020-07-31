from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BathingSpotForm, StationForm, FeatureDataForm
from .models import BathingSpot, Station, FeatureType
from django.urls import reverse
# Create your views here.


def index(request):
    entries = BathingSpot.objects.all()
    return render(request, "ews/index.html", {"entries": entries})


def create_spot(request):
    if request.method == "POST":
        form = BathingSpotForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data["name"]
            id = BathingSpot.objects.filter(name =name).values()[0]["id"]
        return HttpResponseRedirect(reverse('ews:detail', args=[id]))
    else:
        form = BathingSpotForm()
    return render(request, "ews/create.html", {"form":form})

def detail_view(request, spot_id):
    entries = BathingSpot.objects.get(id = spot_id)
    stations = entries.stations.values()
    #featuretype = []
    
    for i in range(len(stations)):
        stations[i]["feature_type"] = FeatureType.objects.get(id = stations[i]['feature_type_id'])
    
    return render(request, "ews/detail.html", {"entries": entries, "stations":stations})



def add_station(request):
    if request.method == "POST":
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('ews:index'))
    else:
        form = StationForm()
       
    return render(request, "ews/add_station.html", {"form":form})

def add_data(request):
    if request.method == "POST":
        form = FeatureDataForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('ews:add_station'))
    else:
        form = FeatureDataForm()
    return render(request, "ews/add_data.html", {"form":form})
