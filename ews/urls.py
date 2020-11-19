from django.urls import path
from . import views


app_name = "ews"
urlpatterns=[
# List Views
path("bathingspots", views.bathingspots, name="bathing_spots"),
path("stations", views.stations, name="stations"),
path("", views.mlmodels, name="mlmodels"),

#authorization
#path("login", views.login_view, name="login"),
#path("logout", views.logout_view, name="logout"),
path("register", views.register, name="register"),

# create views
path("spot_create", views.spot_create, name="spot_create"),
path("model_config", views.model_config, name="model_config"),
path("model_delete/<int:model_id>", views.delete_model, name="delete_model"),

path("add_station", views.add_station, name="add_station"),
path("delete_station/<int:station_id>", views.delete_station, name="delete_station"),
path("station_detail/<int:station_id>", views.station_detail, name="station_detail"),

# ??
path("detail/<int:spot_id>", views.detail_view, name = "detail"),
path("file_upload/<int:station_id>", views.file_upload, name="file_upload"),
]