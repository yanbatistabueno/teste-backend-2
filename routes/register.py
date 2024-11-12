from flask import Blueprint, render_template, request, redirect
from database.user import create_user, get_current_date, get_user, encrypt_password
register_route = Blueprint("register", __name__)




@register_route.route("/")
def register():
    return render_template("register.html")

@register_route.route("/", methods=["POST"])
def register_create_user():
    new_password =  encrypt_password(request.form.get("password"), str(get_current_date()))
    create_user(username=request.form.get("username"), email=request.form.get("email"), password=new_password, role=request.form.get("role"))
    return redirect("/login")

