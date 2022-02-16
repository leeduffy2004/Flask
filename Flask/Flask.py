from flask import Flask

App = Flask(__name__)

@App.route("/aboutus")
def message():
    return "Hello My Friends"

@App.route("/NBS")
def boom():
    return "Welcome to Nationwide"

App.run()
