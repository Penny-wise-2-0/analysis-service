from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()
db = SQLAlchemy()
Base = automap_base()  

def create_app():
    app = Flask(__name__, template_folder="template")
    app.config["SQLALCHEMY_DATABASE_URI"] =  os.getenv("DATABASE_URL").replace("postgresql://", "cockroachdb://")
    db.init_app(app)
    CORS(app)
    with app.app_context():
        Base.prepare(db.engine, reflect=True) 

  
    from routes.registerRoutes import register_routes
    register_routes(app, db)
    migrate = Migrate(app, db)

    return app