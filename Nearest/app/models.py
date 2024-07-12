from django.contrib.gis.db import models
from django.contrib.auth.models import User

class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.PointField()
