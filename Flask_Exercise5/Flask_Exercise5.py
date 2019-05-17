from flask import Flask, render_template

app = Flask(__name__)


# Bind '/' and '/userName' with the function that return a dynamic template
@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)