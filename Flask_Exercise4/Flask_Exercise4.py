# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 17th, 2019
# -------------------------------------------------------------------------

from flask import Flask, render_template

app = Flask(__name__)


# Generating an html page using a template ("profile.html" with variable called "name")
@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)