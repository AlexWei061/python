from math import *
from flask.views import View
from flask import Blueprint, url_for, render_template, request, jsonify, send_from_directory
from flask_login import login_required
import os
import pymongo
from bson import json_util

app_api = Blueprint('app_api', __name__)


# 连接到mongodb
def connect_db(dbname):
    MONGO_URI = "mongodb://127.0.0.1:27017/"
    client = pymongo.MongoClient(MONGO_URI)
    db = client[dbname]
    return db


def find_data(col, all=True, filter=None, limit = 50):
    # filter = {"tagname":"Code"}  #example filter

    mydb = connect_db("alex_db")
    if all == True:
        return mydb[col].find()
    else:
        return mydb[col].find(filter).limit(limit)

def get_translation(word):
    pairs = find_data("trans_table", all=False, filter={"word":{"$regex":".*"+word+".*"}})
    ret = []
    for pair in pairs:
        ret.append({"word": pair['word'], "trans": pair['trans']})
    return ret


def add_new_web(col, web):
    mydb = connect_db("alex_db")
    mydb[col].update_one({"tagname": web["tag"]},
                         {"$push": {"webs": {"$each": [{"webname": web['name'], "url": web['url']}]}}})

# 运算
@app_api.route('/api/calculate')
def add_numbers():
    calc_expression = request.args.get('calc_expression', 0, type=str)
    try:
        result = eval(calc_expression)
    except Exception as e:
        result = "Please input the correct expression!"
    return jsonify(result = result)


@app_api.route('/api/collected_web')
def collected_webs():
    mywebs = find_data("myweb", all=True)
    return (json_util.dumps(mywebs))

    '''
    with open("myweb.json", 'r', encoding="UTF-8") as load_f:
        webdata = json.load(load_f)
        return jsonify(webdata)
    '''


@app_api.route('/api/add_url')
def process_add_web():
    tagname = request.args.get('tagname', 0, type=str)
    webname = request.args.get('webname', 0, type=str)
    weburl = request.args.get('weburl', 0, type=str)
    web = {
        "tag" : tagname,
        "name" : webname,
        "url" : weburl
    }
    add_new_web("myweb", web)
    return jsonify("refresh page to see the result")

@app_api.route('/api/translate')
def translate():
    trans_expression = request.args.get('trans_expression', 0, type=str)
    print(trans_expression)
    pairs = find_data("trans_table", all=False, filter={"word":{"$regex":".*"+trans_expression+".*"}})
    ret = []
    for pair in pairs:
        ret.append((pair['word'], pair['trans']))
    return jsonify(result = ret)

