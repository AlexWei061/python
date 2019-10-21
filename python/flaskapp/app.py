from math import *
from flask.views import View
from flask import Blueprint, url_for, render_template, request, jsonify, send_from_directory
from flask_login import login_required
import os
import pymongo
from bson import json_util


# 连接到mongodb
def connect_db(dbname):
    MONGO_URI = "mongodb://192.168.56.101:27017/"
    client = pymongo.MongoClient(MONGO_URI,
                                 username='admin',
                                 password='1739456',
                                 authSource='admin',
                                 authMechanism='SCRAM-SHA-256')
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

@app.route("/world")
@login_required
def world():
    return "Hello World from app 2!"


@app.route("/")
@login_required
def hello():  # This is my home page
    return render_template("myweb__home.html")


# @login_required
class HelloView(View):
    @login_required
    def dispatch_request(self, lang=None):  # This is my codes
        if lang == None:
            return render_template('mycodes.html')
        elif lang == "c++":
            return render_template('c++.html')
        elif lang == "python":
            return render_template("python.html")
        elif lang == "java":
            return render_template("java.html")


view = HelloView.as_view('mycodes')
app.add_url_rule('/mycodes', view_func=view)
app.add_url_rule('/mycodes/<lang>', view_func=view)


@app.route('/test/jquery/calculator')
@login_required
def test_jquery():
    return render_template("jquery.html")


@app.route('/backend-dbweb')
def backend_dbwebs():
    mywebs = find_data("myweb", all=True)
    return render_template("backend_dbweb.html", tags=mywebs)


@app.route('/frontend-dbweb')
def front_dbwebs():
    return render_template("frontend_dbweb.html")

