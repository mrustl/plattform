from django.db import models

# Create your models here.


class BathingSpot(models.Model):
    name=models.CharField(max_length= 64)
    def __str__(self):
        return f"{self.name}"

class FeatureType(models.Model):
    name=models.CharField(max_length=64)
    unit=models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Station(models.Model):
    name=models.CharField(max_length=64)
    feature_type=models.ForeignKey(FeatureType, on_delete=models.CASCADE, related_name="feature_type")
    bathing_spot=models.ManyToManyField(BathingSpot, blank = True, related_name="stations")
    def __str__(self):
        return f"{self.name}"

class FeatureData(models.Model):
    date=models.DateTimeField()
    value= models.DecimalField(max_digits=6, decimal_places=2)
    station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name="data")
    
