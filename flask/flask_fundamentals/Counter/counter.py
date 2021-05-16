
from flask import Flask, render_template, request, session
from werkzeug.utils import redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route("/")
def home():
    if "time" not in session:
        session["time"] = 0
    if "count" not in session:
        session["count"] = 0
    session["time"] += 1 #hoe i do not add by i when ever i come from redirect
    count = session["count"]
    time = session["time"]
    return render_template("index.html", count=count, time=time)

@app.route("/add2")
def add2():
    # if "count" not in session:
    #     session["count"] = 0
    session["count"] += 2
    count = session["count"]
    time = session["time"]
    return render_template("index.html", count = count, time=time)

@app.route("/addnumber", methods=["POST"])
def add_number():
    # if "count" not in session:
    #     session["count"] = 0
    session["count"] += int(request.form["text1"])
    count = session["count"]
    time = session["time"]
    return render_template("index.html", count = count, time=time)

@app.route("/clear", methods=["POST"])
def clear():
    session.clear()
    return redirect("/")

if __name__== "__main__":
    app.run(debug=True)
