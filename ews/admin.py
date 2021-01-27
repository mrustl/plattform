from django.contrib.gis import admin
from .models import BathingSpot, Site, FeatureData, FeatureType, PredictionModel, SelectArea
from import_export.admin import ImportExportModelAdmin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdminMixin


@admin.register(FeatureData)
class featuredataAdmin(ImportExportModelAdmin):
    list_display=("id", "date", "value", "site")

   

#@admin.register(Bathing)
class BathingSpotAdmin(admin.ModelAdmin):
    list_display=("id", "name", "user")

   

class FeatureTypeAdmin(admin.ModelAdmin):
    list_display=("id", "name", "unit")

    

#class SiteAdmin(admin.ModelAdmin):
 #   list_display=("id", "name", "owner", "feature_type")

    pass
#admin.site.register(Site, LeafletGeoAdmin)
class SiteAdmin(LeafletGeoAdmin):
    list_display=("id", "name", "feature_type")

class SelectAreaAdmin(LeafletGeoAdmin):
    list_display=("id", "name", "feature_type")

admin.site.register(BathingSpot,BathingSpotAdmin)
admin.site.register(Site, SiteAdmin)

admin.site.register(SelectArea, SelectAreaAdmin)
admin.site.register(PredictionModel)
admin.site.register(FeatureType, FeatureTypeAdmin)
