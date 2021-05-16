from flask import Flask, render_template, redirect,request
from flask.helpers import url_for
app = Flask(__name__)

@app.route("/")
def dojo_login():
    location = ["Palestine", "China", "Japan"]
    gender = ["Female", "Male"]
    language = ["Python","Marne","Java","JavaScript"]
    return render_template("index.html", location=location, gender=gender, language=language)

@app.route("/userinfo", methods=["POST"])
def user_info():
    list = []
    for i in request.form:
        list.append(request.form[i])
    return render_template("user_info.html",list=list)

if __name__ == "__main__":
    app.run(debug=True)