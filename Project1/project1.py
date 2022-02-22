from flask import Flask, render_template, request, redirect
import mysql.connector

app=Flask(__name__)

db=mysql.connector.connect( host="localhost",
                            user="root",
                            password="root",
                            database="employeerecords"
                            )
mycursor=db.cursor()

@app.route("/")
def homepage():
    mycursor.execute("Select * from personal")
    records=mycursor.fetchall();

    return render_template("homepage.html", data=records)

@app.route("/departments/<dept>")
def departmentlist(dept):
    mycursor.execute("Select * from personal where department='"+dept+"'")
    records=mycursor.fetchall();

    return render_template("homepage.html", data=records)

@app.route("/newrecord")
def newrecord():
    return render_template("newrecord.html")

@app.route("/saverecord",methods=["post"])
def saverecord():
    name=request.form["na"]
    dept=request.form["dept"]
    mycursor.execute("insert into personal(name,department) values('{0}','{1}')".format(name,dept))
    db.commit()
    return redirect("/")

@app.route("/details/<empid>")
def details(empid):
    mycursor.execute("Select * from personal where empid="+empid)
    personalrecords=mycursor.fetchall();
    mycursor.execute("Select * from accounts where empid="+empid)
    salaryrecords=mycursor.fetchall();
    return render_template("details.html", personal=personalrecords, accounts=salaryrecords)

app.run(debug=True)

