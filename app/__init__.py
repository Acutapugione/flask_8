from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<host>/<database_name>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_cw_8:Qwerty12345%@localhost/flask_db'

db = SQLAlchemy(app)


from app import models, routes

with app.app_context():
    db.create_all()