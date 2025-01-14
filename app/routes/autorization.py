from flask import Blueprint, render_template, request, redirect, flash, session
from ..extentions import db
from ..config import PASSWORD, LOGINN

autoriz = Blueprint('autoriz', __name__)

@autoriz.route("/autorization", methods=["POST", "GET"])
def LOGIN():
    print("rqMethod is ", request.method)
    if request.method == "POST":
        login = str(request.form["login"])
        password = str(request.form["password"])
        if login == LOGINN and password == PASSWORD:
            session['user'] = login  
            session['role'] = 'admin'
            return redirect("/")
        else:
            return redirect("/autorization")
    else:
        return render_template("autorization.html")
    
