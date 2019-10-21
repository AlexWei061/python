import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route("/")
def plan():
    return render_template('plan.html')


app.debug = True
if __name__ == '__main__':
    app.run(debug=True)
