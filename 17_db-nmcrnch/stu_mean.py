#Mai Mushroomz -- Jason Lin, Mai Rachlevsky
#SoftDev1 pd07
#K17 -- Average
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="foo.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

# Returns the average grade given a student id
def get_average(student_id):
    command = "SELECT peeps.id, mark FROM courses, peeps WHERE peeps.id = courses.id"
    c.execute(command)
    total_grade = 0
    total_classes = 0
    # Iterates through all the course grades and sums up the grades associated with the student
    for student_grades in c:
        if student_grades[0] == student_id:
            total_grade += student_grades[1]
            total_classes += 1
    avg_grade = total_grade / total_classes
    return avg_grade

# Returns a list of list of averages in the format [[name,id,average],...]
def get_all_avg():
    command = "SELECT name, peeps.id FROM peeps"
    c.execute(command)
    all_students = c.fetchall()
    all_averages = []
    # Adds a list of format [name,id,average] into the list of all averages
    for student in all_students:
        all_averages.append([student[0],student[1],get_average(student[1])])
    return all_averages

# Creates the table of all averages
def create_avg_table():
    command = "CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)"
    c.execute(command)

# Populates the table with all the averages
def populate():
    all_average = get_all_avg()
    # Iterates through the list from the get_all_avg function and adds it to the table
    for student in all_average:
        command = 'INSERT INTO peeps_avg VALUES({0},{1})'.format(student[1],student[2])
        c.execute(command)

# Adds a course to the table
def add_courses(course_name,grade,student_id):
    command = 'INSERT INTO courses VALUES("{0}",{1},{2})'.format(course_name,grade,student_id)
    c.execute(command)
    db.commit();

#Tests
print(get_all_avg())
create_avg_table()
populate()
add_courses("physics",87,5)
db.commit()

db.close() #close database
