import json

from flask import request
from backend.app import app
from backend.app.Encoder import AlchemyEncoder
from backend.app.db.CreditCard import CreditCard
from backend.app.db.Transaction import Transaction
from backend.app.db.User import User


@app.route("/viewTransactionHistory", methods=['POST'])
def viewTransactionHistory():
    req = request.json
    senderId = req["id"]
    user = User.query.filter_by(id='{}'.format(senderId)).one()
    creditCard = CreditCard.query.filter_by(user_id='{}'.format(senderId)).one()

    c = Transaction.query.filter_by(sender='{}'.format(user.email)).all()
    c += Transaction.query.filter_by(reciever='{}'.format(user.email)).all()
    c += Transaction.query.filter_by(reciever='{}'.format(creditCard.number)).all()
    return json.dumps(c, cls=AlchemyEncoder)


