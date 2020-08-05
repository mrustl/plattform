from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BathingSpotForm, StationForm, FeatureDataForm
from .models import BathingSpot, Station, FeatureType
from django.urls import reverse
from tablib import Dataset, core
from .resources import FeatureDataResource
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    entries = BathingSpot.objects.filter(user = request.user)
    peter=request.user
    return render(request, "ews/index.html", {"entries": entries, 'peter':peter})

@login_required
def create_spot(request):
    peter=request.user
    spot = BathingSpot()
    if request.method == "POST":
        form = BathingSpotForm(request.POST)
        form.user = peter
        if form.is_valid():
            spot.name = form.cleaned_data["name"]
            spot.user = peter
            spot.save()
            name = form.cleaned_data["name"]
            id = BathingSpot.objects.filter(name =name).values()[0]["id"]
        return HttpResponseRedirect(reverse('ews:detail', args=[id]))
    else:
        form = BathingSpotForm()
          
    return render(request, "ews/create.html", {"form":form, 'peter':peter})

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
    if request.method == "POST":
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('ews:index'))
    else:
        form = StationForm()
       
    return render(request, "ews/add_station.html", {"form":form})
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
def file_upload(request):
    if request.method == 'POST':

        rainfall_resource = RainfallResource()
        dataset = Dataset()
        new_rainfall = request.FILES['myfile']


        imported_data = dataset.load(new_rainfall.read().decode("utf-8"), format="csv")
      #  create an array containing the location_id
        location_arr = [bathingspot_id] * len(imported_data)

        # use the tablib API to add a new column, and insert the location array values
        imported_data.append_col(location_arr, header="bathingspot")

        try:
            result = rainfall_resource.import_data(dataset, dry_run=True)  # Test the data import
        except Exception as e:
            return HttpResponse(e, status=status.HTTP_400_BAD_REQUEST)

        if not result.has_errors():
            rainfall_resource.import_data(dataset, dry_run=False)  # Actually import now

    #    y_data =  np.array(Rainfall.objects.filter(bathingspot=bathingspot_id).values_list('value', flat = True))
     #   x_data = np.array(Rainfall.objects.filter(bathingspot=bathingspot_id).values_list('datetime', flat = True))

    #    plot_div = plot([go.Scatter(x=x_data, y=y_data,
     #                       mode='lines+markers', name='test',
      #                      opacity=0.8, marker_color='rgba(0, 86, 110, 1)')],
       #                     output_type='div')
        template = loader.get_template('berlin/view_import.html')
        context = {
            'plot_div': plot_div,
            'bathingspot_id': bathingspot_id,

            'img_url': img_url,
        }
        return HttpResponse(template.render(context, request))
    return render(request, 'berlin/import.html')
