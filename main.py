import requests
import googlemaps
from gmplot import gmplot
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyC0dEPMVePlBkEaqSs6O4l-E-sOcyawvOE')


r = requests.get('http://api.open-notify.org/iss-now.json')
result = r.json()

location = result['iss_position']
latitude = location['latitude']
longitude = location['longitude']

print('latitude:', latitude)
print('longitude:', longitude)

latitudefloat = float(latitude)
longitudefloat = float(longitude)

reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
print(reverse_geocode_result)


google_maplot = gmplot.GoogleMapPlotter(latitude, longitude, 13)

google_maplot.apikey = 'AIzaSyC0dEPMVePlBkEaqSs6O4l-E-sOcyawvOE'

hidden_gem_lat, hidden_gem_lon = latitudefloat, longitudefloat
google_maplot.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

google_maplot.draw("my_map.html")
