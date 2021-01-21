from django.contrib import admin
from ews.models import BathingSpot, Site, FeatureData, FeatureType, PredictionModel
from import_export.admin import ImportExportModelAdmin



@admin.register(FeatureData)
class featuredataAdmin(ImportExportModelAdmin):
    list_display=("id", "date", "value", "site")

    pass

#@admin.register(Bathing)
class BathingSpotAdmin(admin.ModelAdmin):
    list_display=("id", "name", "user")

    pass

class FeatureTypeAdmin(admin.ModelAdmin):
    list_display=("id", "name", "unit")

    pass

class SiteAdmin(admin.ModelAdmin):
    list_display=("id", "name", "owner", "feature_type")

    pass

admin.site.register(BathingSpot,BathingSpotAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(PredictionModel)
admin.site.register(FeatureType, FeatureTypeAdmin)
