from flask import Flask,render_template

App = Flask(__name__)

@App.route("/info1")
def HomePage1():
    return render_template("information.html", na="Lee", addr="Livingston", color="red")

@App.route("/info2")
def HomePage2():
    return render_template("information.html", na="David", addr="London", color="grey")

@App.route("/info3")
def HomePage3():
    return render_template("information.html", na="Russell", addr="San Francisco", color="orange")

App.run()