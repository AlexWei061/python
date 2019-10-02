from math import *
from flask.views import View
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
import json

app = Blueprint('app',__name__)

@app.route("/world")
@login_required
def world():
    return "Hello World from app 2!"

@app.route("/")
@login_required
def hello():                                                    # This is my home page
    return render_template("myweb__home.html")

@app.route("/urls")
@login_required
def websites():
    return render_template("urls.html")


#@login_required
class HelloView(View):
    @login_required
    def dispatch_request(self, lang=None):                      # This is my codes
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

# 四则运算
@app.route('/api/calculate')
def add_numbers():
    calc_expression = request.args.get('calc_expression', 0, type=str)
    try:
        result = eval(calc_expression)
    except Exception as e:
        result = "Please input the correct expression!"
    return jsonify(result = result)

@app.route('/api/collected_web')
def collected_webs():
    with open("myweb.json", 'r', encoding="UTF-8") as load_f:
        webdata = json.load(load_f)
        print(webdata)
        return jsonify(webdata)


@app.route('/backend-dbweb')
def backend_dbwebs():
    with open("myweb.json", 'r', encoding="UTF-8") as load_f:
        mywebs = json.load(load_f)
        return render_template("backend_dbweb.html", tags = mywebs)


@app.route('/frontend-dbweb')
def front_dbwebs():
    return render_template("frontend_dbweb.html")
