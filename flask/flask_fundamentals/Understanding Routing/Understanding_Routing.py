from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1 style="text-align:center";> "Hello World!" </h1>'

@app.route("/dojo")
def dojo():
    return '<h1 style="text-align:center";> "Dojo!" </h1>'

@app.route("/say/<name>")
def say_name(name):
    return f'<h1 style="text-align:center";> "Hi {name}!" </h1>'

@app.route("/repeat/<int:num>/<word>")
def repeat_word(num,word):
    return f'<h1 style="text-align:center";> "{word}" </h1> '* num

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '<h1 style="text-align:center";> "It\'s Invalid Entry"</h1><p style="text-align:center"> Try <mark>/say/"any name"</mark> or <mark>/repeat/"any nymber"/"any word"</mark></p> '


if __name__ == "__main__":
    app.run(debug=True)