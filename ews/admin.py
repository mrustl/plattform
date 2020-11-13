from django.contrib import admin
from ews.models import BathingSpot, Station, FeatureData, FeatureType
from import_export.admin import ImportExportModelAdmin

# Register your models here.

#class FeatureDataAdmin(admin.ModelAdmin):
 #   list_display=("id", "date", "value", "station")

#class StationAdmin(admin.ModelAdmn):
 #   filter_horizontal=()

@admin.register(FeatureData)
class featuredataAdmin(ImportExportModelAdmin):
    list_display=("id", "date", "value", "station")

    pass

#@admin.register(Bathing)
class BathingSpotAdmin(admin.ModelAdmin):
    list_display=("id", "name", "user")

    pass

class FeatureTypeAdmin(admin.ModelAdmin):
    list_display=("id", "name", "unit")

    pass

class StationAdmin(admin.ModelAdmin):
    list_display=("id", "name", "owner", "feature_type")

    pass

admin.site.register(BathingSpot,BathingSpotAdmin)
admin.site.register(Station, StationAdmin)
#admin.site.register(FeatureData, FeatureDataAdmin)
admin.site.register(FeatureType, FeatureTypeAdmin)
