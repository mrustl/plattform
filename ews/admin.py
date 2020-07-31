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


admin.site.register(BathingSpot)
admin.site.register(Station)
#admin.site.register(FeatureData, FeatureDataAdmin)
admin.site.register(FeatureType)
