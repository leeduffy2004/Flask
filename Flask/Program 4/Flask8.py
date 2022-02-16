from flask import Flask,render_template

App = Flask(__name__)

@App.route("/info1/<Name1>/<Salary1>")
def HomePage1(Name1,Salary1):
    
    return render_template("SalarySlip2.html",Name=Name1,Salary=int(Salary1))

App.run()