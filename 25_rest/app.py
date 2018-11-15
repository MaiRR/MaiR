# Mai Rachlevsky
# SoftDev1 pd7
# K25 -- Getting more REST
# 2018-11-15

from flask import Flask, render_template
import urllib
import json


app = Flask(__name__)
poem = urllib.request.urlopen("https://www.poemist.com/api/v1/randompoems")
response = poem.read()
data = json.loads(response)



@app.route("/")
def homepage():
    return render_template("poem.html", title = data[0]["title"], content =  data[0]["content"])

if __name__ == "__main__":
    app.debug = True
    app.run()
