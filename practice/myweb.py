import flask
#from flask import Flask
import flask_login
import os
from flask_login import UserMixin
from flask_login import LoginManager


app = flask.Flask(__name__)

app.secret_key = 'weitongyue\' key'  # Change this!

app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.login_message = u"用户未登录，请先登录。"
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self):  # 最好从数据库获取，或使用加密方式获取，这里只简单示例
        self.id = 1
        self.username = 'root'
        self.password = '123'

    # 注意！这里必须重写，因为源码使用unicode(id)，但是python3没有unicode()方法！此时就无法登录用户！
    def get_id(self):
        return self.id

    @staticmethod
    def get(user_id):
        """try to return user_id corresponding User object.
        This method is used by load_user callback function
        """
        if not user_id:
            return None
        try:
            if user_id == 1:  # 最好从文件或数据库读取id（这里为简单写死为1了）
                return User()
        except:
            return None
        return None



#@login_manager.user_loader
#def load_user(userid):
#    return User.get(userid)


# Our mock database.
users = {'foo@bar.tld': {'password': 'secret'}}



@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('/home'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

@app.route('/home')
@flask_login.login_required
def hello_home():
    return '''this is my home page'''

@app.route('/')
@flask_login.login_required
def hello_world():
    return '''Hello web'''

@app.route("/bear")
def bear():
    return """
        <html>
          <head>
            <title>398572380</title>
          </head>
           <body>
             <h1>The Brown Bear</h1>
             <div id="introduction">
               <h2>About Brown Bears</h2>
               <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern</strong>.<br /><br /> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
               <h3>Species</h3>
               <ul>
                 <li>Arctos</li>
                 <li>Collarus</li>
                 <li>Horribilis</li>
                 <li>Nelsoni (extinct)</li>
               </ul>
               <h3>Features</h3>
               <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
             </div>
             <div id="habitat">
               <h2>Habitat</h2>
               <h3>Countries with Large Brown Bear Populations</h3>
               <ol>
                 <li>Russia</li>
                 <li>United States</li>
                 <li>Canada</li>
               </ol>
               <h3>Countries with Small Brown Bear Populations</h3>
               <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
             </div>
             <div id="media">
               <h2>Media</h2>
               <img src="https://s3.amazonaws.com/codecademy-content/courses/web-101/web101-image_brownbear.jpg" alt="A Brown Bear"/>
                   <video src="https://s3.amazonaws.com/codecademy-content/courses/freelance-1/unit-1/lesson-2/htmlcss1-vid_brown-bear.mp4" width="320" height="240" controls>Video not supported</video>
             </div>
           </body>
        </html>   
"""





app.debug = True
if __name__ == '__main__':
    app.run(debug = True)
