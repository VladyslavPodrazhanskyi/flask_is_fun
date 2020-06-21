# app/__init__.py

import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash

from config import dev

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app(config_type): #dev, test or prod
    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(), 'config', config_type + ".py")
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'authentication.do_the_login'
    login_manager.session_protection = 'strong'

    bcrypt.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app









