from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", x=8, y=8,color1 = "#9379bb", color2 = "rgb(193, 208, 240)")

@app.route("/<int:x>")
def row_number(x):
    return render_template("index.html", x=x, y=8,color1 = "#9379bb", color2 = "rgb(193, 208, 240)")

@app.route("/<int:x>/<int:y>")
def column_number(x,y):
    return render_template("index.html", x=x, y=y, color1 = "#9379bb", color2 = "rgb(193, 208, 240)")

@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def board_color(x,y,color1,color2):
    return render_template("index.html", x=x, y=y, color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug=True)