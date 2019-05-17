# -------------------------------------------------------------------------
#   Author: Quang Tran
#   Date: May 15th, 2019
# -------------------------------------------------------------------------

from flask import Flask

# Write __name__ inside to let Flask app identify the root path (later will need)
app = Flask(__name__)


@app.route('/')     # 'route()' will bind a function to a URL
def hello():        # By convention, name this func the same name as your web page
    return "Welcome to my home page"


if __name__ == "__main__":
    app.run(debug=True)