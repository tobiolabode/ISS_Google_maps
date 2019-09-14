from flask import Flask, render_template
from main import longitudefloat, latitudefloat, List_of_names, List_desciptions, links_for_images

app = Flask(__name__, template_folder=".")
# GoogleMaps(app, key="AIzaSyC0dEPMVePlBkEaqSs6O4l-E-sOcyawvOE")

@app.route("/")
def mapview():
    # marker = '6495ED.png'
    latitude = latitudefloat
    longitude = longitudefloat
    Names_of_austronuts = List_of_names
    desciptions = List_desciptions
    Links = links_for_images
    return render_template('From_google.html', latitude=latitude, longitude=longitude,
                           Names_of_austronuts=Names_of_austronuts,
                           desciptions=desciptions, Links=Links)




if __name__ == "__main__":
    app.run(debug=True)
