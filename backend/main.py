from flask import Flask, request
import json
import random
from OnlineAccount import OnlineAccount
from User import User
from CreditCard import CreditCard


app = Flask(__name__)
user = '{"id": "0", "ime": "", "prezime": "", "adresa": "", "grad": "", "drzava": "", "brTelefona": "", "email": "", "lozinka": ""}'
x = []

creditCard = CreditCard(1, "Max Verstappen", "30.05.2022.", 225883)
user = User(0, "", "", "", "", "", "", "", "", 1)

@app.route("/register", methods=['POST'])
def register():
    req = request.json
    print(req)
    user.set_id(req["id"])
    user.set_name(req["ime"])
    user.set_lastname(req["prezime"])
    user.set_address(req["adresa"])
    user.set_city(req["grad"])
    user.set_country(req["drzava"])
    user.set_phoneNumber(req["brTelefona"])
    user.set_email(req["email"])
    user.set_password(req["lozinka"])
    user.set_verified(False)
    print(user)
    print("SUPER MAX")
    return "Successfully registered."

@app.route("/login", methods=['POST'])
def login():
    req = request.json
    if(req["password"] == user.password and req["email"] == user.email):
        return json.dumps(user.__dict__)
    else:
        return "Invalid email."

@app.route("/changeAccount", methods=['POST'])
def changeAccount():
    req = request.json
    user.set_id(req["id"])
    user.set_name(req["ime"])
    user.set_lastname(req["prezime"])
    user.set_address(req["adresa"])
    user.set_city(req["grad"])
    user.set_country(req["drzava"])
    user.set_phoneNumber(req["brTelefona"])
    user.set_email(req["email"])
    user.set_password(req["lozinka"])
    return "Updated."

@app.route("/accountVerification", methods=['POST'])
def accountVerification():
    req = request.json

    if(creditCard.get_number() == int(req["broj"]) and creditCard.get_csc() == int(req["sigurnosniKod"])):
        user.set_verified(True)
        creditCard.set_balance(creditCard.get_balance() - 1)
        print("Verified.")
        return json.dumps(user.__dict__)
    else:
        print("Not verified")
        return "Verification failed."

    return "Azurirano."


if __name__=="__main__":
    app.run(host="0.0.0.0")