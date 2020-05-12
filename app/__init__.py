from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'passphrase'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:project2@localhost/project2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

UPLOAD_FOLDER_PP = './app/static/uploads'
UPLOAD_FOLDER_POST = './app/static/uploads/pic'
db = SQLAlchemy(app)


app.config.from_object(__name__)
app.config['UPLOAD_FOLDER_PP'] = UPLOAD_FOLDER_PP
app.config['UPLOAD_FOLDER_POST'] = UPLOAD_FOLDER_POST
from app import views

