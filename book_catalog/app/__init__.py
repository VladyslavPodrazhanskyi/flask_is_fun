# app/__init__.py

import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import dev

db = SQLAlchemy()

def create_app(config_type): #dev, test or prod
    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(), 'config', config_type + ".py")
    app.config.from_pyfile(configuration)

    db.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    return app









