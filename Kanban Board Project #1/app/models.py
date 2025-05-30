from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(50))
    password_hashed = db.Column(db.String(200))
    notes = db.relationship('Note', backref='owner', lazy=True)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    column = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    