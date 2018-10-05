# Tarkus -- Theodore Peters, Mai Rachlevsky
# SoftDev1 pd7
# k16 -- No Trouble
# 2018-10-05


import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

db = sqlite3.connect('datta.db') #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
c.execute("CREATE TABLE nerds(name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")

csvfile = open('raw/peeps.csv')
reader = csv.DictReader(csvfile)
for row in reader:
    c.execute("INSERT INTO nerds VALUES('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ");")
csvfile.close()

csvfile = open('raw/courses.csv')
c.execute ("CREATE TABLE teacher_reviews(code TEXT, mark INTEGER, id);")
reader = csv.DictReader(csvfile)
for row in reader:
    c.execute("INSERT INTO teacher_reviews VALUES('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ");")
csvfile.close()

db.commit()

c.execute("SELECT * FROM nerds;")
print(c.fetchall())
c.execute("SELECT * FROM teacher_reviews")
print(c.fetchall())
db.close()  #close database
