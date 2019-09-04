import requests
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyC0dEPMVePlBkEaqSs6O4l-E-sOcyawvOE')


r = requests.get('http://api.open-notify.org/iss-now.json')
result = r.json()

location = result['iss_position']
latitude = location['latitude']
longitude = location['longitude']

print('latitude:', latitude)
print('longitude:', longitude)


reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
print(reverse_geocode_result)
