# app/auth/models.py

from datetime import datetime
from app import db, bcrypt, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now())


    # classmethod belogs to the class but not associated with any instance of the class
    @classmethod
    def create_user(cls, name, email, password):
        user = cls(
            name=name,
            email=email,
            user_password=bcrypt.generate_password_hash(password).decode('utf-8')
        )

        db.session.add(user)
        db.session.commit()

        return user

    def check_pass(self, password):
        return bcrypt.check_password_hash(self.user_password, password)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)