from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
def test_form():
    return render_template('forms.html')

@app.route('/auth', methods=["GET", "POST"])
def authenticate():
    if request.method == "GET":
        name = request.args['username']
    else:
        name = request.form['username']
    method = request.method
    return render_template('welcome.html',name=name,method=method)


if __name__ == "__main__":
    app.debug = True
    app.run()

