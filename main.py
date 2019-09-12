import requests
import googlemaps
from gmplot import gmplot
import wikipedia


gmaps = googlemaps.Client(key='AIzaSyC0dEPMVePlBkEaqSs6O4l-E-sOcyawvOE')


r = requests.get('http://api.open-notify.org/iss-now.json')
result = r.json()


r = requests.get('http://api.open-notify.org/astros.json')
astronauts_names = r.json()



astronauts_in_space = astronauts_names['people']

List_of_names = []

for person in astronauts_in_space:
    print(person['name'])
    List_of_names.append(person['name'])

number_in_space = astronauts_names['number']
print('Number of people in space:', number_in_space)

print(List_of_names)

# import pdb; pdb.set_trace()

for every_person in List_of_names:
    print('-------------------------' * 3, end='\n')

    if every_person == 'Andrew Morgan':
        every_person = 'Andrew R. Morgan'

    if every_person == 'Alexander Skvortsov':
        print('IF STATEMENT' * 5)
        every_person = 'Aleksandr Skvortsov (cosmonaut)'

    print(wikipedia.summary(every_person))




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
