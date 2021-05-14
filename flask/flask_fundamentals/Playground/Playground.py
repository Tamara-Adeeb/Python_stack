from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", num=3, color ="orange")

@app.route("/play/<int:num>")
def box_number(num):
    return render_template("index.html",num=num, color ="orange")

@app.route("/play/<int:num>/<color>")
def box_color(num,color):
    return render_template("index.html", num = num, color = color)

if __name__=="__main__":
    app.run(debug=True)