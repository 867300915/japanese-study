from flask import Flask
from markupsafe import Markup
app = Flask(__name__)
@app.route("/")
def hello_world():
    return Markup("<p>Hello, World!<p/>")