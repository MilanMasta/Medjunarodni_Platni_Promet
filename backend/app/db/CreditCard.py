from backend.app import db

class CreditCard(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    expirationDate = db.Column(db.String(8), nullable=False)
    csc = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)