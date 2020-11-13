from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BathingSpot(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bathing_spots")
    name=models.CharField(max_length= 64)
    description = models.CharField(max_length = 200, default = " ")
    def __str__(self):
        return f"{self.name}"

class FeatureType(models.Model):
    name=models.CharField(max_length=64)
    unit=models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Station(models.Model):
    name=models.CharField(max_length=64)
    owner=models.ForeignKey(User, on_delete=models.PROTECT, related_name="owner")
    feature_type=models.ForeignKey(FeatureType, on_delete=models.CASCADE, related_name="feature_type")
    bathing_spot=models.ManyToManyField(BathingSpot, blank = True, related_name="stations")
    def __str__(self):
        return f"{self.name}"

class FeatureData(models.Model):
    date=models.DateTimeField()
    value= models.DecimalField(max_digits=6, decimal_places=2)
    station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name="station")
    
class PredictionModel(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = "models")
    bathing_spot = models.ForeignKey(BathingSpot, on_delete=models.CASCADE, related_name="models")
    station = models.ManyToManyField(Station, related_name = "models")
