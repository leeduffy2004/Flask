from flask import Flask,render_template

App = Flask(__name__)

@App.route("/info1")
def HomePage1():
    return render_template("SalarySlip1.html",Name="Heidi",Salary=1000)

App.run()