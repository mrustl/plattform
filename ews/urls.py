from django.urls import path
from . import views


app_name = "ews"
urlpatterns=[
# List Views
path("bathingspots", views.bathingspots, name="bathing_spots"),
path("sites", views.sites, name="sites"),
path("", views.mlmodels, name="mlmodels"),

#authorization
#path("login", views.login_view, name="login"),
#path("logout", views.logout_view, name="logout"),
path("register", views.register, name="register"),

# create views
path("spot_create", views.spot_create, name="spot_create"),
path("model_config", views.model_config, name="model_config"),
path("model_delete/<int:model_id>", views.delete_model, name="delete_model"),
path("model_edit/<int:model_id>", views.model_edit, name="model_edit"),

path("add_site", views.add_site, name="add_site"),
path("delete_site/<int:site_id>", views.delete_site, name="delete_site"),
path("site_detail/<int:site_id>", views.site_detail, name="site_detail"),

path("selectarea_create", views.selectarea_create, name="selectarea_create"),
# ??
path("detail/<int:spot_id>", views.detail_view, name = "detail"),
path("file_upload/<int:site_id>", views.file_upload, name="file_upload"),
path('model_fit/<int:model_id>', views.model_fit, name ='model_fit'),
path('prediction_switch/<int:model_id>', views.prediction_switch, name ='prediction_switch')
]