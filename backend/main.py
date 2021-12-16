from flask import Flask, request
import json
import random
from OnlineAccount import OnlineAccount
from User import User
from CreditCard import CreditCard


app = Flask(__name__)
#user = '{"id": "0", "name": "", "lastname": "", "address": "", "city": "", "country": "", "phoneNumber": "", "email": "", "password": ""}'
x = []
creditCard = CreditCard(1, "Max Verstappen", "30.05.2022.", 225883)
user = User(0, "", "", "", "", "", "", "", "", 1)
users={}         # dict -> key = id && value = user
creditCards={creditCard} # dict -> key = creditCardNum && value = creditCard
usersCount=0



@app.route("/register", methods=['POST'])
def register():
    req = request.json
    print(req)
    user.set_id(usersCount+1) # setting id with global counter
    usersCount += 1
    user.set_name(req["name"])
    user.set_lastname(req["lastname"])
    user.set_address(req["address"])
    user.set_city(req["city"])
    user.set_country(req["country"])
    user.set_phoneNumber(req["phoneNumber"])
    user.set_email(req["email"])
    user.set_password(req["password"])
    user.set_verified(False)
    
    users[user.get_email()]=user
    return "Successfully registered."

@app.route("/login", methods=['POST'])
def login():
    req = request.json
    if req["email"] in users:  
        if User(users[req["email"]]).get_password() == req["password"]:
             return json.dumps(user.__dict__)
        else:
            return "Invalid password."
    else:
        return "User doesn't exits."
    
@app.route("/changeAccount", methods=['POST'])
def changeAccount():
    req = request.json
    #user.set_id(req["id"])
    for i in users:
        if i.id==req["id"]:
            user=i
    user.set_name(req["name"])
    user.set_lastname(req["lastname"])
    user.set_address(req["address"])
    user.set_city(req["city"])
    user.set_country(req["country"])
    user.set_phoneNumber(req["phoneNumber"])
    user.set_email(req["email"])
    user.set_password(req["password"])
    for i in users:
        if i.id==req["id"]:
            users.remove(i)
            break;
    users[req["id"]]=user
    return "Updated."

@app.route("/accountVerification", methods=['POST'])
def accountVerification():
    req = request.json
    if req["number"] in creditCards:
        if (creditCards[int(req["number"])]).get_csc() == int(req["csc"]) : 
            if (creditCards[int(req["number"])]).get_expirationDate() == int(req["expirationDate"]):
                if req["email"] in users:
                    users[req["email"]].set_verified(True)
                creditCards[int(req["number"])].withdraw(1)
                print("Verified.")
                return json.dumps(user.__dict__)
    if(creditCard.get_number() == int(req["number"]) and creditCard.get_csc() == int(req["csc"])):
        if req["email"] in users:
            users[req["email"]].set_verified(True)
        creditCard.set_balance(creditCard.get_balance() - 1)
        print("Verified.")
        return json.dumps(user.__dict__)
    else:
        print("Not verified")
        return "Verification failed."

    return "Azurirano."

@app.route("/depositOnAccount", methods=['POST'])
def depositOnAccount():
    req = request.json
    print(req["amount"])
    if(int(req["amount"]) <= creditCard.get_balance()):
        user.set_onlineAccountBalance(int(req["amount"]))
        print("DEPOSIT DONE.")
        return json.dumps(user.__dict__)
    else:
        print("DEPOSIT FAILED.")
        return "Deposit failed."



if __name__=="__main__":
    app.run(host="0.0.0.0")