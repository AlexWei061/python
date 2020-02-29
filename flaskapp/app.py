from math import *
from flask.views import View
from flask import Blueprint, url_for, render_template, request, jsonify, send_from_directory
from flask_login import login_required
import os
import pymongo
from bson import json_util


# 连接到mongodb
def connect_db(dbname):
    MONGO_URI = "mongodb://127.0.0.1:27017/"
    client = pymongo.MongoClient(MONGO_URI)
    db = client[dbname]
    return db


def find_data(col, all=True, filter=None):
    # filter = {"tagname":"Code"}  #example filter
    mydb = connect_db("alex_db")
    if all == True:
        return mydb[col].find()
    else:
        return mydb[col].find(filter)


def add_new_web(col, web):
    mydb = connect_db("alex_db")
    mydb[col].update_one({"tagname": web["tag"]},
                         {"$push": {"webs": {"$each": [{"webname": web['name'], "url": web['url']}]}}})


app = Blueprint('app', __name__)


@app.route("/")
@login_required
def hello():  # This is my home page
    return render_template("myweb__home.html")


# @login_required
class MyCodes(View):
    @login_required
    def dispatch_request(self, lang = None):  # This is my codes
        if lang == None:
            return render_template('mycodes.html')
        elif lang == "c++":
            return render_template('c++.html')
        elif lang == "python":
            return render_template("python.html")
        elif lang == "java":
            return render_template("java.html")

my_codes_view = MyCodes.as_view('mycodes')
app.add_url_rule('/mycodes', view_func = my_codes_view)
app.add_url_rule('/mycodes/<lang>', view_func = my_codes_view)

class Games(View):
    # @app.route('/games')
    @login_required
    def dispatch_request(slef, lang = None):
        if lang == None:
            return render_template("games.html")
        else:
            return "Hello"

games_view = Games.as_view('games')
app.add_url_rule('/games', view_func = games_view)
app.add_url_rule('/games/<lang>', view_func = games_view)

'''
@app.route('/games')
#@login_required
def test_games():
    return "xxxxx"

'''


@app.route('/test/jquery/calculator')
@login_required
def test_jquery():
    return render_template("jquery.html")


@app.route('/backend-dbweb')
@login_required
def backend_dbwebs():
    mywebs = find_data("myweb", all=True)
    return render_template("backend_dbweb.html", tags=mywebs)

@app.route('/happynewyear')
@login_required
def happy_new_year():
    return render_template("newyear.html")
