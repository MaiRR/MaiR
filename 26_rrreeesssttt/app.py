# Mai Rachlevsky
# SoftDev1 pd7
# K25 -- Getting more REST
# 2018-11-15


import urllib.request as urlrequest
from urllib.request import urlopen
from flask import Flask, render_template
import json, urllib


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
key = '325077-Inspyre-THCC3LLO'
req = urlrequest.Request('https://tastedive.com/api/similar?q=titanic&info=1&k=' + key, headers={'User-Agent': 'Mozilla/5.0'})
r = urlopen(req).read()
d = json.loads(r.decode('utf-8'))



@app.route("/")
def homepage():
    return render_template("base.html", dog = data, sun = times["results"]["sunrise"] + ' and ' + times["results"]["sunset"] , holiday = h, d=d['Similar']['Info'][0]['Name'] + ':' + d['Similar']['Info'][0]['wTeaser'])



if __name__ == "__main__":
    app.debug = True
    app.run()
