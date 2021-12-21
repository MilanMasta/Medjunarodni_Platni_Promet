import datetime

from backend.app.db.Balances import Balances
from backend.app.db.User import User
from backend.app.db.CCards import CCards
from backend.app.db.CreditCard import CreditCard
from flask import request
from backend.app import app
from backend.app.db import db



@app.route("/depositOnAccount", methods=['POST'])
def depositOnAccount():
    req = request.json
    amount = int(req["amount"])
    userId= req["id"]

    kar = CreditCard.query.filter_by(user_id='{}'.format(userId)).one()
    user = User.query.filter_by(id='{}'.format(userId)).one()
    rsdBalanceUser = Balances.query.filter_by(user_id='{}'.format(userId),valute="RSD").one()
    if(kar.balance - amount >= 0):
        kar.balance -= amount
        rsdBalanceUser.balance +=amount
        db.session.commit()
        return user.userToJSON()
    else:
        return "Deposition failed."




#     print()
#     print()
#     if int() in users:
#         user=users[int(req["id"])]
#     pom_creditCard=None
#     if user.get_creditCardNum()  in creditCards:
#         pom_creditCard=creditCards[user.get_creditCardNum()]
#     if((int(req["amount"]) + int(req["rsdBalance"]))  <= pom_creditCard.get_balance()):
#         users[user.get_id()].depositRSDOnAccount(int(req["amount"]))
#         return user.userToJSON()
#     else:
#         print("DEPOSIT FAILED.")
#
