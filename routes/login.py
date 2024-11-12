from flask import Blueprint, render_template, request, redirect, session
from database.user import get_user
login_route = Blueprint("login", __name__)

@login_route.route("/")
def login():
    return render_template("login.html")

@login_route.route("/", methods=["POST"])
def login_check_user():
    user = get_user(request.form.get("username"), request.form.get("password"))
    if(user == None):
        session["user"] = False
        return render_template("login.html", acesso="false")
    else:
        session["user"] = True
        return redirect("/data")


@login_route.route("/loggout")
def loggout():
    if(session["user"] == True):
        session["user"] = False
        return render_template("login.html", loggout=True)
    else:
        return redirect("/login")
