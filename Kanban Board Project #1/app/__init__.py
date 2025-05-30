from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd92c48b77213333fe5c311c40618525a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'

db = SQLAlchemy(app)
login = LoginManager(app)

login.login_view = "login"

from app import routes
