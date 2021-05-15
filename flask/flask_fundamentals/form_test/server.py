from flask import Flask, render_template, request,redirect
from flask.globals import request
from flask.helpers import flash, url_for
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/user", methods=["POST"])
def user():
    user_name = request.form["name"]
    user_email = request.form["email"]
    if user_name == "" or user_email == "":
        return redirect(url_for("login"))#how i can redirect to function and pass new parameters in my case a new massage
    else:
        return render_template("show.html", user_name=user_name,user_email=user_email)


if __name__=="__main__":
    app.run(debug=True)