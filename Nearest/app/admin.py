from django.contrib import admin
from .models import UserLocation
from leaflet.admin import LeafletGeoAdmin


class TaxiDriverAdmin(LeafletGeoAdmin):
    list_display = ['user', 'location']


admin.site.register(UserLocation, TaxiDriverAdmin)
