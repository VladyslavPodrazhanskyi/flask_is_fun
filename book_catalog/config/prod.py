import os

DEBUG = False
SECRET_KEY = b'H\xa9U<>\xa8\xfaO\x07\xbd\xec\xe1bJnk\xd0\xf7j\xceW\x8a\xe7/'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False