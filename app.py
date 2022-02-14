from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    hetgetal = 25
    if hetgetal < 20:
        return "<p>Hello, Wereld!"+str(hetgetal)+", echt we nieuwe spullen</p>"
    else:
        return "het is groter dan 20"

@app.route("/tweede/<voornaam>")
def hello_world2(voornaam):
    return f"<p>Hello {voornaam}, anderefunctie</p>"