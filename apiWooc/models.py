from django.db import models

# Create your models here.


class Parcel(models.Model):
    """docstring for Parcel."""
    woocID = models.IntegerField()
    woocUser = models.IntegerField()
    name = models.CharField(max_length=200)
    #geom = models.PolygonField()
