#Mai Rachlevksy
#SoftDev1 pd7
#k08 -- Fill Yer Flask
#2018-09-20


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello!"

@app.route("/ask")
def ask():
   return "How are you?"

@app.route("/greeting")
def greeting():
    return "How can I help you?"


if __name__ == "__main__":
    #app.debug = True
    app.run()


 

