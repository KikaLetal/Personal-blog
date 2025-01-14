from flask import Flask
from .extentions import db, migrate
from .routes.index import main
from .routes.Post import Post
from .routes.autorization import autoriz
from .routes.LogOut import LogOut
from .config import *


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = config.SECRET_KEY

    app.register_blueprint(LogOut)
    app.register_blueprint(main)
    app.register_blueprint(Post)
    app.register_blueprint(autoriz)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()
    return app

