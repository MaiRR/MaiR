#Peter Cwalina, Mai Rachlevsky -- Mai Spaggeti
#SoftDev1 pd 7
#K14 -- Do I Know You?
#2018-10-01
from flask import Flask, render_template, request,url_for,session,redirect,flash
import os
app = Flask(__name__)
app.secret_key = os.urandom(32)
#dictionary of logins with key = user and value is the password
logins = {"hackerMan":"el1te"}

@app.route("/")
def log():
    #if a logged in session exists
    if 'loggedIn' in session:
        #render a greeting via template
        return render_template('greet.html',
                               user = session['loggedIn'],
                               greeting = "Hello"
                               )
    #otherwise you provide the login form
    else:
        return render_template('form.html')

@app.route("/auth", methods=["POST","GET"])
def authenticate():
    #if you didnt use the form lets redirect you back to the root
    if request.method == "GET":
        return redirect(url_for('log'))
    
    #the submited username
    user = request.form['username']
    #if the username exists within our login dict
    if user in logins:
        #check if the password matches
        if request.form['password'] == logins[user]:
            #then create a logged in session with the username as the value
            session['loggedIn'] = user
            #then redirect back to the root for the greeting
            return redirect(url_for('log'))
        #if password doesnt match render the form with the appropriate error
        else:
            flash('Password is incorrect')
            return render_template('form.html')
                                  
    #if the username does not exist return the form with the appropriate error
    else:
        flash('Error Username not found')
        return render_template('form.html')
            
    
@app.route("/logout")
def logout():
    #just incase you try to logout when not logged in
    if 'loggedIn' in session:
        #remove the current session
        session.pop('loggedIn')
        #redirect back to the root for another login form
        return redirect(url_for('log'))
    else:
        #back to the root you go
        return redirect(url_for('log'))
    
if __name__ == "__main__" :
    app.debug = True
    app.run()
