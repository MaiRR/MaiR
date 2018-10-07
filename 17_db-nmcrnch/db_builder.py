#Mai Mushroomz -- Jason Lin, Mai Rachlevsky
#SoftDev1 pd07
#K17 -- Average
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="foo.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

# Create and populate the courses table
csvfile = open('data/courses.csv')
reader = csv.DictReader(csvfile)
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)
for row in reader:
    command = 'INSERT INTO courses VALUES("{0}",{1},{2})'.format(row['code'], row['mark'], row['id'])
    c.execute(command)

# Create and populate the courses table
csvfile = open('data/peeps.csv')
reader = csv.DictReader(csvfile)
command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"
c.execute(command)
for row in reader:
    command = 'INSERT INTO peeps VALUES("{0}",{1},{2})'.format(row['name'], row['age'], row['id'])
    c.execute(command)

db.commit() #save changes
