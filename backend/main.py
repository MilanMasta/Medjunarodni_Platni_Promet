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
    print(user)
    return "Successfully registered."

@app.route("/login", methods=['POST'])
def login():
    req = request.json
    if req["email"] in users:  
        if User(users[req["email"]]).get_password() == req["password"]:
             return user.userToJSON()
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
                if int(req["id"]) in users:
                    users[int(req["id"])].set_verified(True)
                else:
                    return "Id for verification doesn't exists."
                creditCards[int(req["number"])].withdraw(1)
                print("Verified.")
                return user.userToJSON()
            else:
                return "Invalid expiration date."
        else:
            return "Invalid CSC."
    else:
        return "Verification failed."

@app.route("/depositOnAccount", methods=['POST'])
def depositOnAccount():
    req = request.json
    print(req["amount"])
    print(req["rsdBalance"])
    #imacemo i email u req -> (req["email"])
    #ISPRAVKA: trebali bismo da imamo id u req a ne email jer imamo dict u kom je kljuc id usera
    # stoga-> 
    if int(req["id"]) in users:
        user=users[int(req["id"])]
    pom_creditCard=None
    if user.get_creditCardNum()  in creditCards:
        pom_creditCard=creditCards[user.get_creditCardNum()]
    if((int(req["amount"]) + int(req["rsdBalance"]))  <= pom_creditCard.get_balance()):
        users[user.get_id()].depositRSDOnAccount(int(req["amount"]))
        print("Successfully deposited.")
        return user.userToJSON()
    else:
        print("DEPOSIT FAILED.")
        return "Deposition failed." # promenila sam string za return ali ne vidim gde na frontu treba da ga izmenim



if __name__=="__main__":
    app.run(host="0.0.0.0")