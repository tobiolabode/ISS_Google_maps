import requests
import googlemaps
from gmplot import gmplot
import wikipedia
from bs4 import BeautifulSoup
import requests


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

List_desciptions = []
links_for_images = []
Link_of_page = []




for every_person in List_of_names:
    print('-------------------------' * 3, end='\n')

    if every_person == 'Andrew Morgan':
        every_person = 'Andrew R. Morgan'

    if every_person == 'Alexander Skvortsov':
        every_person = 'Aleksandr Skvortsov (cosmonaut)'

    print(wikipedia.summary(every_person))
    List_desciptions.append(wikipedia.summary(every_person))
    Link_of_page.append(wikipedia.page(every_person).url)


for every_link in Link_of_page:
    print('---------NEW PERSON----------------' * 3, end='\n')
    HTTP_results = requests.get(every_link)
    page_results = HTTP_results.content

    soup = BeautifulSoup(page_results, 'html.parser')
    infocard = soup.find('table', class_='infobox biography vcard')
    image_tags = infocard.findAll('img')

    links_image_tags = []
    for image_tag in image_tags:
        print(image_tag.get('src'))
        links_image_tags.append(image_tag.get('src'))

    links_for_images.append(links_image_tags[0])


print('----------------------')
for i in links_for_images:
    print(i)



location = result['iss_position']
latitude = location['latitude']
longitude = location['longitude']

print('latitude:', latitude)
print('longitude:', longitude)

latitudefloat = float(latitude)
longitudefloat = float(longitude)

reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
print(reverse_geocode_result)


google_maplot = gmplot.GoogleMapPlotter(latitude, longitude, 4)

google_maplot.apikey = 'AIzaSyC0dEPMVePlBkEaqSs6O4l-E-sOcyawvOE'

hidden_gem_lat, hidden_gem_lon = latitudefloat, longitudefloat
google_maplot.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

google_maplot.draw("my_map.html")
