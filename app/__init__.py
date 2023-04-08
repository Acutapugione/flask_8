from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password>@<host>/<database_name>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password>@<host>/database'

db = SQLAlchemy(app)

from app import models, routes