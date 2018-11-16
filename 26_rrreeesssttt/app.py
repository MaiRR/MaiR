# Mai Rachlevsky
# SoftDev1 pd7
# K25 -- Getting more REST
# 2018-11-15

from flask import Flask, render_template
import urllib
import json


app = Flask(__name__)
dog = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
response = dog.read()
data = json.loads(response)
sun = urllib.request.urlopen("https://api.sunrise-sunset.org/json?lat=40&lng=20")
suntime = sun.read()
times = json.loads(suntime)
url = urllib.request.urlopen("https://holidayapi.com/v1/holidays?key=030efe42-1b7c-4c4e-a8f4-79cd091aa6bc&country=IL&year=2018&month=3")
result = url.read()
holiday = json.loads(result)
h = holiday["holidays"]



@app.route("/")
def homepage():
    return render_template("base.html", dog = data, sun = times["results"]["sunrise"] + ' and ' + times["results"]["sunset"] , holiday = h )

if __name__ == "__main__":
    app.debug = True
    app.run()
