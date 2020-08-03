from django.urls import path
from . import views


app_name = "ews"
urlpatterns=[
path("", views.index, name="index"),
path("create_spot", views.create_spot, name="create"),
path("detail/<int:spot_id>", views.detail_view, name = "detail"),
path("add_station", views.add_station, name="add_station"),
path("add_data", views.add_data, name="add_data"),
path("file_upload", views.add_data, name="file_upload")

]