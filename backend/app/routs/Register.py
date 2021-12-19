from backend.app.db.User import User

from flask import request
from backend.app import app
from backend.app.db import db

@app.route("/register", methods=['GET', 'POST'])
def register():
    req = request.json
    user = User(name=req["name"], lastname=req["lastname"], address=req["address"], city=req["city"],
                country=req["country"], phoneNumber=req["phoneNumber"], email=req["email"], password=req["password"],
                verified=False)
    try:
        db.session.add(user)
        db.session.commit()
        return "Successfully registered." # mejl je jedinstven posalji pozitivan odg
    except:
        print("Mejl vec postoji") # na fron treba staviiti ocekivan odgovor kada mejl vec postoji i staviti ga ispod u return
        return "greska"