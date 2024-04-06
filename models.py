from app import Base, db
from app import Base


def setup_database(app):
    with app.app_context():
        Base.prepare(db.engine, reflect=True)

Transaction = Base.classes.transactions