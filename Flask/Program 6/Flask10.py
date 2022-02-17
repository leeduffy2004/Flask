from flask import Flask, render_template, request
App = Flask(__name__)

@App.route("/")
def homePage():

    return render_template("inputform.html")

@App.route("/data", methods=["post"])
def process():

    A=int(request.form["num1"])
    B=int(request.form["num2"])

    return render_template("TimesTable.html", T=A,R=B)

App.run(debug=True)

