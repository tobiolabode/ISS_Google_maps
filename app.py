from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from main import longitudefloat, latitudefloat

app = Flask(__name__, template_folder=".")
GoogleMaps(app, key="AIzaSyC0dEPMVePlBkEaqSs6O4l-E-sOcyawvOE")

@app.route("/")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=latitudefloat,
        lng=-longitudefloat,
        markers=[(latitudefloat, -longitudefloat)]
    )

    return render_template('home.html', mymap=mymap)


if __name__ == "__main__":
    app.run(debug=True)
