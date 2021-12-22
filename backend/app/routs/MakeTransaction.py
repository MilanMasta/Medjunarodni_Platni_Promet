from flask import request
from backend.app import app
from backend.app.db import db
from backend.app.db.Balances import Balances
from backend.app.db.CreditCard import CreditCard
from backend.app.db.Transaction import Transaction
from backend.app.db.User import User


@app.route("/makeTransaction", methods=['POST'])
def makeTransaction():
    req = request.json
    senderId = req["id"]
    user = User.query.filter_by(id='{}'.format(senderId)).one() #user posiljalac
    amount = float(req["amount"])
    reciever = req["reciever"]
    destination = req["destination"]

    if(destination == "banka"):
        try:
            creditCard = CreditCard.query.filter_by(number='{}'.format(reciever)).one()
            senderBalance = Balances.query.filter_by(user_id='{}'.format(senderId), valute='RSD').one()
            senderBalance.balance -= amount
            creditCard.balance += amount
            tra = Transaction(state="U obradi", sender=f"{user.email}" , reciever=f"{creditCard.number}",amount=amount,destination="Banka")
            db.session.add(tra)
            db.session.commit()
            return user.userToJSON()
        except:
            return "Transaction failed."
    else:
        try:
            recieverUser = User.query.filter_by(email='{}'.format(reciever),verified=True).one()
            recieverBalance = Balances.query.filter_by(user_id='{}'.format(recieverUser.id),valute='RSD').one()
            senderBalance = Balances.query.filter_by(user_id='{}'.format(senderId),valute='RSD').one()
            senderBalance.balance -= amount
            recieverBalance.balance += amount
            tra = Transaction(state="U obradi", sender=f"{user.email}" , reciever=f"{recieverUser.email}",amount=amount,destination="Online racun")
            db.session.add(tra)
            db.session.commit()
            return user.userToJSON()
        except:
            return "Transaction failed."