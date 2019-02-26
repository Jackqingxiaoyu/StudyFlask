from . import main
from flask import render_template
from app.models import Student

@main.route("/index")
def index():
    return render_template("index.html")