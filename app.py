from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from main import longitudefloat, latitudefloat

app = Flask(__name__, template_folder=".")
# GoogleMaps(app, key="AIzaSyC0dEPMVePlBkEaqSs6O4l-E-sOcyawvOE")

@app.route("/")
def mapview():
    # marker = '6495ED.png'
    latitude = latitudefloat
    longitude = longitudefloat
    return render_template('From_google.html', latitude=latitude, longitude=longitude)




if __name__ == "__main__":
    app.run(debug=True)
