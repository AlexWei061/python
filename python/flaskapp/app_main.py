from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user

from app import app

app_main = Flask(__name__)
app_main.register_blueprint(app)

# config
app_main.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app_main)
login_manager.login_view = "login"


# silly user model
class User(UserMixin):
    def __init__(self, id, name=None, passwd=None):
        self.id = id
        self.name = name
        self.passwd = passwd

    def get_id(self):
        return self.id


# some protected url
@app_main.route('/test')
@login_required
def test():
    return Response("Test Page!")


# somewhere to login
@app_main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "ty.wei@foxmail.com" and password == "myweb":
            id = username
            user = User(id)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username placeholder='input your email'>
            <p><input type=password name=password placeholder='input your password'>
            <p><input type=submit value=Login>
        </form>
        ''')


# somewhere to logout
@app_main.route("/logout")
@login_required
def logout():
    logout_user()
    return Response("""<p>Logged out</p>
                       <a href="/">Go back ro home page</a>""")


# handle login failed
@app_main.errorhandler(401)
def page_not_found(e):
    return Response("""<p>Login failed</p>
                       <a href="/">Try Again</a>""")


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)

if __name__ == "__main__":
    app_main.run()