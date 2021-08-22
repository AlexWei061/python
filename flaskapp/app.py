from math import *
from flask import *
from flask.views import View
from flask import Blueprint, url_for, render_template, request, jsonify, send_from_directory
from flask_login import login_required
import os
import pymongo
from app_api import *
from bson import json_util


# 连接到mongodb
def connect_db(dbname):
    MONGO_URI = "mongodb://127.0.0.1:27017/"
    client = pymongo.MongoClient(MONGO_URI)
    db = client[dbname]
    return db


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
            return render_template('my_codes/c++.html')
        elif lang == "python":
            return render_template("my_codes/python.html")
        elif lang == "java":
            return render_template("my_codes/java.html")

my_codes_view = MyCodes.as_view('mycodes')
app.add_url_rule('/mycodes', view_func = my_codes_view)
app.add_url_rule('/mycodes/<lang>', view_func = my_codes_view)

class Games(View):
    @login_required
    def dispatch_request(slef, lang = None):
        game_list = ["game1"]
        if lang == None:
            return render_template("my_games/games.html")
        elif lang in game_list:
            add_str = 'my_games/' + lang + '.html'
            return render_template(add_str)
        else:
            return """<h1>It is under production</h1>"""

games_view = Games.as_view('games')
app.add_url_rule('/games', view_func = games_view)
app.add_url_rule('/games/<lang>', view_func = games_view)



class Collections(View):
    def dispatch_request(self, domain=None):
        col_list = ['happy_new_year']
        if domain == None:
            return render_template("my_collections/collections.html")
        elif domain in col_list:
            add_str = 'my_collections/' + domain + '.html'
            return render_template(add_str)
        else:
            return """<h1>It is under production</h1>"""

cols_view = Collections.as_view('collections')
app.add_url_rule('/collections', view_func = cols_view)
app.add_url_rule('/collections/<domain>', view_func = cols_view)


class Study(View):
    def dispatch_request(self, domain = None):
        study_list = ['calculator', 'translator', 'rand_generator']
        if domain == None:
            return render_template('my_study/study.html')
        elif domain == "translator":
            search_phrase = request.args.get('word')
            if search_phrase == None:
                return render_template('my_study/translator_backend.html', data={})
            else:
                data = {"search_phrase":search_phrase}
                trans_table = get_translation(search_phrase)
                data["trans_table"] = trans_table
                return render_template('my_study/translator_backend.html', data=data)

        elif domain in study_list:
            add_str = 'my_study/' + domain + '.html'
            return render_template(add_str)
        else:
            return '''It is under production'''

study_view = Study.as_view('stduy')
app.add_url_rule('/study', view_func = study_view)
app.add_url_rule('/study/<domain>', view_func = study_view)


@app.route('/backend-dbweb')
@login_required
def backend_dbwebs():
    mywebs = find_data("myweb", all=True)
    return render_template("backend_dbweb.html", tags=mywebs)

@app.route('/happynewyear')
@login_required
def happy_new_year():
    return render_template("my_collections/.html")
