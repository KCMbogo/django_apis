from django.shortcuts import render
from django_countries import countries
from .utils import *
import requests


def index(request):
    data, current_lat, current_lon = get_current_location()
    target_lat, target_lon = get_target_location()
    distance = calculate_distance(current_lat, current_lon, target_lat, target_lon)
    # regions = get_country_regions(data['countryCode'])
    shiping_price = 18 * 0.05 * (distance / 1000) + 18
    context = {
        'data': data,
        'distance': distance,
        'countries': countries,
        # 'regions':  regions,
        'shiping_price': shiping_price,
    }
    return render(request, 'location/index.html', context)


#  US
# Latitude: 34.0544
# Longitude: -118.2441