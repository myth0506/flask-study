from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from datetime import datetime



app = Flask(__name__)

bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def index():
         return render_template('index.html',
                                current_time=datetime.utcnow())

# @app.route('/')
# @app.route('/index')
# def index():
#     user = { 'nickname': 'Miguel' } # fake user
#     return render_template("index.html",
#         title = 'Home',
#         user = user)

# @app.route('/user/<name>')
# def user(name):
# return render_template("user.html",
#                        name = name)


@app.route('/user/<name>')
def user(name):
    return render_template('test/user.html', name=name)




  # if __name__ == '__main__':
  #     manager.run(host='127.0.0.1', port=8000)

if __name__ == '__main__':
         app.run(host='127.0.0.1', port=8000)