from flask_sqlalchemy import SQLAlchemy as sql
from flask_migrate import Migrate
db = sql()
migrate = Migrate()