from flask import Flask

App = Flask(__name__)

@App.route("/")
def HomePage():
    return """
    <html>
    <center> <h1> <b> Welcome to Nationwide </b> </h1>
    We are the largest building society in the UK
    <br>
    <br>
    <a href="http://localhost:5000/Team"> Who we are </a> <br>
    <a href="http://localhost:5000/Services"> Our Services </a> <br>

    </html>
    """ 

@App.route("/Team")
def message():
    return """
    <html>
    <B> This is our Team </B>
    <br>
    <a href="http://localhost:5000"> Home </a>
    <br>
    <ul>
        <li> <u> CEO - Lee  </u> </li>
        <li> <i> Chairman - David </i> </li>
        <li> <b> Secretary - Michael </b> </li>
    </ul>
    </html>
    """ 

@App.route("/Services")
def boom():
    return """
    <html>
    <h2> <B> We Provide the following Services </B> </h2>
    <br>
    <a href="http://localhost:5000"> Home </a>
    <br>
    <ul>
        <li> <u> Open Account </u> </li>
        <li> <i> Deposit Money </i> </li>
        <li> <b> Withdraw Money </b> </li>
    </ul>
    </html>
    """ 
App.run()