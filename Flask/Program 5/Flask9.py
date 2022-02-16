from flask import Flask,render_template

App = Flask(__name__)

@App.route("/")
def HomePage1():
    
    return render_template("HomePage.html")

@App.route("/TimesTable/<num>")
def TimesTable(num):
    return render_template("/TimesTable.html", T=int(num))

App.run()