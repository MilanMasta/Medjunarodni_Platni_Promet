import copy
import json
from backend.app.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    phoneNumber = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    creditCards = db.relationship('CreditCard', backref='id', lazy=True)

    def userToJSON(self):
        pom = copy.deepcopy(self)
        pom.onlineAccount = pom.onlineAccount.__dict__
        return json.dumps(pom.__dict__)