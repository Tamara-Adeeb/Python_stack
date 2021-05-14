from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return '<h1 style="text-align:center;" > Hello There!</h1> <p style="text-align:center;">Welcome to my first webpage</p>'

@app.route("/<name>")
def user(name):
    return f'<h1 style="text-align:center;" > Hello {name} </h1><p style="text-align:center;">Welcome ! <br> We are happy to have you</p>'

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(port="5001", debug=True)
