from flask import Flask, render_template
from flask.templating import render_template_string

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    # DB Access
    like_foods = [
        "자장면",
        "부대찌게",
        "닭발",
        "콩국수",
        "삼겹살",
    ]
    return render_template("profile.html", like_foods=like_foods)


@app.route("/posts")
def post_list():
    return render_template("post_list.html")
