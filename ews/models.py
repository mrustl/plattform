from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField, MultiPolygonField
# Create your models here.


class BathingSpot(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bathing_spots")
    name = models.CharField(max_length= 64)
    description = models.CharField(max_length = 200, default = " ")
    def __str__(self):
        return f"{self.name}"

class FeatureType(models.Model):
    name = models.CharField(max_length=64)
    unit = models.CharField(max_length=64, null = True)
    def __str__(self):
        return f"{self.name}"

class Site(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ref_name =  models.CharField(max_length=64, null = True )
    geom = PointField(null = True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="owner")
    feature_type = models.ForeignKey(FeatureType, on_delete=models.CASCADE, related_name="feature_type")
    
    def __str__(self):
        return f"{self.name}"
    
    @property
    def popupContent(self):
      return '<a href="site_detail/{}"><strong>{}</strong></a> <p> {}</p>'.format(
          self.id,
          self.name,
          self.feature_type)
    @property
    def SiteType(self):
        return '{}'.format(self.feature_type)
#"{% url 'ews:site_detail' entry.id  %}"
class FeatureData(models.Model):
    date = models.DateTimeField()
    value = models.DecimalField(max_digits=1000, decimal_places=3)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="site")
    class Meta:
        unique_together = ('date', 'site','value',)
    
class PredictionModel(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = "models")
    bathing_spot = models.ForeignKey(BathingSpot, on_delete=models.CASCADE, related_name="models")
    site = models.ManyToManyField(Site, related_name = "models", null = True, blank = True)
    def __str__(self):
        return f"{self.name}"

class SelectArea(models.Model):
    name = models.CharField(max_length=64)
    geom = MultiPolygonField()
    feature_type = models.ForeignKey(FeatureType, on_delete=models.CASCADE, related_name = "areas")
