from flask import Blueprint, render_template, session, redirect
from database.characters import get_characters, insert_characters, get_current_character
from api.connection import elapsed_time
from api.connection import responseJson
data_route = Blueprint("data", __name__)
import time

import requests



@data_route.route("/")
def data():
    if(session["user"] == True):
        characters = get_characters()
        if (characters == None or len(characters) == 0):
            for c in responseJson["results"]:
                insert_characters(name=c["name"], status=c["status"], image=c["image"], url=c["url"])
            return render_template("data.html", session=True, characters=characters), {"Refresh": "2; url=/data"}
        return render_template("data.html", session=True, characters=characters)
    else:
        return render_template("data.html", session=False)
    
@data_route.route("/<string:name>", methods=["GET"])
def data_character(name):
    if(session["user"] == True):
          character = get_current_character(name=name)
          if (character == None or len(character) == 0):
            return render_template("character-view.html", current_character=None)
          return render_template("character-view.html", current_character=character)
    return redirect("/data")
    