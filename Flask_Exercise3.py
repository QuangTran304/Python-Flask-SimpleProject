# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 16th, 2019
# -------------------------------------------------------------------------

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome! Request method used is: {}".format(request.method)


@app.route("/hello", methods=['GET', 'POST'])
def medthod():
    if request.method == 'POST':
        return "<h3>You are using POST</h3>"
    else:
        return "<h3>You are probably using GET</h3>"


if __name__ == '__main__':
    app.run(debug=True)