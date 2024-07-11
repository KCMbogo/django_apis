import requests
from geopy.distance import geodesic


def get_current_location():
    response = requests.get("http://ip-api.com/json/")

    if response.status_code == 200:
        data = response.json()
    else:
        data = None
    return data, data['lat'], data['lon']


def get_target_location():
    # target_lat, target_lon = -6.57382280, 36.26308460     #dodoma
    target_lat, target_lon = 34.0544,  -118.2441    #USA
    return target_lat, target_lon


def calculate_distance(current_lat, current_lon, target_lat, target_lon):
    current_location = (current_lat, current_lon)
    target_location = (target_lat, target_lon)
    distance = geodesic(current_location, target_location).kilometers
    return distance


def get_country_regions(country_code):
    api = f"https://restcountries.com/v3.1/alpha/{country_code}"

    response = requests.get(api)

    if response.status_code == 200:
        data = response.json()
        country_data = data[0]

        # Get the regions (if available)
        regions = country_data.get("subdivisions", [])
    else:
        regions = None
    
    return regions
