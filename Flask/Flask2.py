from flask import Flask

App = Flask(__name__)

@App.route("/")
def HomePage():
    return "<h1> Welcome to my Home Page </h1>"

@App.route("/aboutus")
def message():
    return "<B> Hello </B> <U> My Friends </U>"

@App.route("/NBS")
def boom():
    return "<B> Welcome to Nationwide </B>"

App.run()