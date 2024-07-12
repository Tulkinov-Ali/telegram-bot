from django.urls import path
from .views import index

urlpatterns = [

    path('', index, name='find_nearest_location'),
]
