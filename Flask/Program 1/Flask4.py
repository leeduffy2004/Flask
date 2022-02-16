from flask import Flask,render_template

App = Flask(__name__)

@App.route("/")
def HomePage():
    return render_template("Home.html")

@App.route("/Team")
def message():
    return render_template("Team.html")

@App.route("/Services")
def boom():
    return render_template("Services.html")

App.run()