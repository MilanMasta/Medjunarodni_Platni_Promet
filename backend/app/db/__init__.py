from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from backend.app import app
import mysql.connector

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sifra@localhost/DataBaseDRS'
db = SQLAlchemy(app)


conection = mysql.connector.connect(
    user='root',
    password='sifra',
    host='localhost'
    )
conection.autocommit = True
sql_cursor = conection.cursor()


class CreditCard(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    expirationDate = db.Column(db.String(8), nullable=False)
    csc = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    phoneNumber = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    creditCards = db.relationship('CreditCard', backref='id', lazy=True)
