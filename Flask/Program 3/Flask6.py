from flask import Flask,render_template

App = Flask(__name__)

@App.route("/info1")
def HomePage1():
    return render_template("SalarySlip.html",Name="Heidi",Salary=10000)

App.run()