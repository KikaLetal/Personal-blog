from .extentions import db
from datetime import datetime

class Article(db.Model):
    # Имя таблицы в базе данных
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.String, default=datetime.now().strftime("%B %d, %Y"))
    title = db.Column(db.String(50), nullable=False)