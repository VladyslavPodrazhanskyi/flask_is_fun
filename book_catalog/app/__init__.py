# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import dev

app = Flask(__name__)


app.config.update(dev)




db = SQLAlchemy()