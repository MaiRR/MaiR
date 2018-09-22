# Team IWantPancakes -- Daniel Keriazis, Mai Rachlevsky
# SoftDev pd7
# K10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
from csv import reader
from util.occupation_handling import csv_to_weighted_list, \
        weighted_choice, read_file

app = Flask(__name__)

# Returns the contents of `csv_file` as a list of lists
def csv_to_list(csv_file):
    with open(csv_file) as f:
        return list(reader(f))

@app.route('/occupations')
def occupations():
    csv_file = 'data/occupations.csv'
    # Strip out first and last lines
    rows = csv_to_list(csv_file)[1:-1]
    occupations = read_file(csv_file)
    weighted_list = csv_to_weighted_list(occupations)
    job = weighted_choice(weighted_list)
    return render_template('occupation_template.html', rows=rows, job=job)

if __name__ == '__main__':
    app.debug = True
    app.run()

