from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return '<h1 style="text-align:center;" > Hello There!</h1> <p style="text-align:center;">Welcome to my first webpage</p>'

@app.route("/<name>")
def user(name):
    return f'<h1 style="text-align:center;" > Hello {name} </h1><p style="text-align:center;">Welcome ! <br> We are happy to have you</p>'

@app.route("/<name1>/<name2>/<name3>")
def users(name1,name2,name3):
    names = [name1,name2,name3]
    new_var = ""
    for i in names:
        new_var += f" <h1 style='text-align:center; '> Hello {i} </h1>\n"

    return f'{new_var} <p style="text-align:center;">Welcome ! <br> We are happy to have you</p>'


@app.route("/admin")
def admin(): # To redirect the user if they enter unauthorized route
    return redirect(url_for("home")) #invoke home function

if __name__ == "__main__":
    app.run(port="5001", debug=True)
