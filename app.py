from flickrapi import FlickrAPI
from flask import Flask
from flask_cors import CORS

FLICKR_PUBLIC = "546f15dfd7ac997a5a92713620c10a10"  # Key for flickrapi
FLICKR_SECRET = "8c8f088139ff65f8"  # secret key for flickrapi
server = "http://localhost:5000"  # localhost server

app = Flask(__name__)  # initialize the app

CORS(app)  # for CORS error

flickr = FlickrAPI(
    FLICKR_PUBLIC, FLICKR_SECRET, format="parsed-json"
)  # connecting to flcikrapi
extras = "url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o"  # extra fetch from api


@app.route("/<search>", methods=["GET"])  # get method for receiving data
def searchImage(search):
    print(search)
    cats = flickr.photos.search(
        text=search, per_page=5, extras=extras
    )  # getting data from search result
    photos = cats["photos"]  # getting array of photos

    return photos


if __name__ == "__main__":
    app.run()


# flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
# extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
