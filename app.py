from flask import Flask, render_template
from main import longitudefloat, latitudefloat, List_of_names, List_desciptions, links_for_images, Link_of_page, Long_name

app = Flask(__name__, template_folder=".")
# GoogleMaps(app, key="AIzaSyC0dEPMVePlBkEaqSs6O4l-E-sOcyawvOE")

@app.route("/")
def mapview():
    latitude = latitudefloat
    longitude = longitudefloat
    Names_of_austronuts = List_of_names
    desciptions = List_desciptions
    Links = links_for_images
    Links_pages = Link_of_page
    Name_of_location = Long_name
    return render_template('From_google.html', latitude=latitude, longitude=longitude,
                           Names_of_austronuts=Names_of_austronuts,
                           desciptions=desciptions,
                           Links=Links,
                           Links_pages=Links_pages,
                           Name_of_location=Name_of_location)




if __name__ == "__main__":
    app.run(debug=True)
