from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['UPLOAD_FOLDER'] = 'app/static/img/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fvptuebrdmqueo:38d955a4da4438435dc5bd721cfba6598f509feaac37e751be545463dc0c7352@ec2-52-6-143-153.compute-1.amazonaws.com:5432/db9hhdmdsdrci0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
