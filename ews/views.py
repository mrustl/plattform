from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BathingSpotForm, StationForm, FeatureDataForm, PredictionModelForm
from .models import BathingSpot, Station, FeatureType, User, PredictionModel
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

def model_config(request):
    if request.method == "POST":
        return HttpResponseRedirect(reverse("ews:index"))
    else:
        pmodel_form = PredictionModelForm
        return render(request, "ews/model_config.html", {"pmodel_form": pmodel_form})





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

        return HttpResponseRedirect(reverse('ews:index'))
    else:
        # prepopulating with dictionary
        form = StationForm()
        user_id = User.objects.filter(username=request.user).values()[0]["id"]
        spot= BathingSpot.objects.filter(user = user_id) 
    return render(request, "ews/add_station.html", {"form":form, "spot":spot})

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
      #  create an array containing the location_id
        location_arr = [station_id] * len(imported_data)

        # use the tablib API to add a new column, and insert the location array values
        imported_data.append_col(location_arr, header="station")

        try:
            result = feature_resource.import_data(dataset, dry_run=True)  # Test the data import
        except Exception as e:
            return HttpResponse(e, status=status.HTTP_400_BAD_REQUEST)

        if not result.has_errors():
            feature_resource.import_data(dataset, dry_run=False)  # Actually import now

    #    y_data =  np.array(Rainfall.objects.filter(bathingspot=bathingspot_id).values_list('value', flat = True))
     #   x_data = np.array(Rainfall.objects.filter(bathingspot=bathingspot_id).values_list('datetime', flat = True))

    #    plot_div = plot([go.Scatter(x=x_data, y=y_data,
     #                       mode='lines+markers', name='test',
      #                      opacity=0.8, marker_color='rgba(0, 86, 110, 1)')],
       #                     output_type='div')
     #   template = loader.get_template('berlin/view_import.html')
      #  context = {
       #     'plot_div': plot_div,
        #    'bathingspot_id': bathingspot_id,

        #    'img_url': img_url,
        #}
        return render(request, "ews/success.html", {'imported_data': imported_data})
    return render(request, 'ews/import.html', {"station_id":station_id})








def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "registration/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "registration/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("ews:index"))
    else:
        return render(request, "registration/register.html")
