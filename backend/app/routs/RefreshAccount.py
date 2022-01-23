from flask import request
from backend.app import app
from backend.app.db import db
from backend.app.db.Balances import Balances
from backend.app.db.CreditCard import CreditCard
from backend.app.db.Transaction import Transaction
from backend.app.db.User import User


@app.route("/refreshAccount", methods=['POST'])
def refreshAccount():
    req = request.json
    senderId = req["id"]
    user = User.query.filter_by(id='{}'.format(senderId)).one()
    return user.userToJSON()