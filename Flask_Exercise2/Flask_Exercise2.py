# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 16th, 2019
# -------------------------------------------------------------------------

from flask import Flask

# Name the app whatever you want to name it
apple = Flask(__name__)


# '@' signifies a decorator => Used to wrap a function and modifying its behavior
@apple.route('/')
def index():
    return "This is some text"


# '<name>' will act as a place holder - a variable
@apple.route('/page/<name>')
def say_hello(name):
    return "<h1>Hello {}, welcome to my page!</h1>".format(name)


if __name__ == '__main__':
    apple.run(debug=True)