import requests

r = requests.get('http://api.open-notify.org/iss-now.json')
result = r.json()

loaction = result['iss_position']
latitude = loaction['latitude']
longitude = loaction['longitude']

print('latitude:', latitude)
print('longitude:', longitude)
