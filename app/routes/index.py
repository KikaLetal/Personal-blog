from flask import Blueprint, render_template, request, redirect, flash, session
from ..extentions import db
from ..models import Article

main = Blueprint('main', __name__)

@main.route("/")
def index():
    posts = reversed(Article.query.all())
    return render_template("index.html", posts=posts)
