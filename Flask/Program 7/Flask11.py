from flask import Flask, render_template, request
App = Flask(__name__)

@App.route("/")
def homePage():
    return render_template("HomePage.html")

@App.route("/Page2/<T>")
def Page2(T):
    return render_template("Page2.html",TimesTable=T)

@App.route("/Page3/<T>/<R>")
def Page3(T,R):
    return render_template("TimesTable.html",TimesTable=int(T), Range=int(R))

App.run(debug=True)