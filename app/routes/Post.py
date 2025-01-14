from flask import Blueprint, render_template, request, redirect, flash
from ..extentions import db
from ..models import Article


Post = Blueprint('Post', __name__)

@Post.route("/CreatePost", methods=["POST", "GET"])
def Create():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]
        post = Article(title=title, text=text) 
        
        try:
            db.session.add(post)
            db.session.commit()
            return redirect("/")
        except Exception as e: 
            db.session.rollback()
            print("произошла ошибка: ", str(e))
            return redirect("/CreatePost")
        finally:
            db.session.remove()
    else:
        return render_template("CreatePost.html")
    

@Post.route("/<int:id>/EditPost", methods=["POST", "GET"])
def Edit(id):
    post = Article.query.get(id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.text = request.form["text"]

        try:
            db.session.commit()
            return redirect("/")
        except Exception as e: 
            db.session.rollback()
            print("произошла ошибка: ", str(e))
            return redirect("/CreatePost")
        finally:
            db.session.remove()


    else:
        return render_template("EditPost.html", post_title=post.title, post_text=post.text)
    


@Post.route("/<int:id>/Delete")
def Delete(id):
    post = Article.query.get(id)

    try:
        db.session.delete(post)
        db.session.commit()
        return redirect("/")
    except Exception as e: 
        db.session.rollback()
        print("произошла ошибка: ", str(e))
        return redirect("/")
    finally:
        db.session.remove()

    

@Post.route("/<int:id>/ARTICLE")
def ARTICLE(id):
    post = Article.query.get(id)
    return render_template("Article.html", post=post)
