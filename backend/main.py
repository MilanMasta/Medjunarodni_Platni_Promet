from flask import request
from flask_sqlalchemy import SQLAlchemy
from backend.app.db import User, CreditCard

# app = Flask(__name__)
# app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqllite:///dataBase.db'
# db = SQLAlchemy(app)

#user = '{"id": "0", "name": "", "lastname": "", "address": "", "city": "", "country": "", "phoneNumber": "", "email": "", "password": ""}'
# x = []
# creditCard = CreditCard(1, "Max Verstappen", "30.05.2022.", 225883)
# user = User(0, "", "", "", "", "", "", "", "", 1)
# users={}         # dict -> key = id && value = user
# creditCards={} # dict -> key = creditCardNum && value = creditCard
# creditCards[creditCard.get_number()] = creditCard
# global usersCount
# usersCount=0





# @app.route("/register", methods=['POST'])
# def register():
#     #trebamo provjeravati da li korisnik sa tim emailom vec postoji!!!!!!!!!!!!!
#     global usersCount
#     req = request.json
#     print(req)
#     user.set_id(usersCount + 1) # setting id with global counter
#     usersCount += 1
#     user.set_name(req["name"])
#     user.set_lastname(req["lastname"])
#     user.set_address(req["address"])
#     user.set_city(req["city"])
#     user.set_country(req["country"])
#     user.set_phoneNumber(req["phoneNumber"])
#     user.set_email(req["email"])
#     user.set_password(req["password"])
#     user.set_verified(False)
#
#     users[user.get_id()]=user
#     print(users)
#     print(user)
#     return "Successfully registered."
#
# @app.route("/login", methods=['POST'])
# def login():
#     req = request.json
#     for key in users:
#         print("LOGIN")
#         print(users[key])
#         if users[key].get_email() == req["email"]:
#             if(users[key].get_password() == req["password"]):
#                 print(users[key].userToJSON())
#                 return users[key].userToJSON()
#             else:
#                 return "Invalid password."
#
#     return "User doesn't exist."
#
#
# @app.route("/changeAccount", methods=['POST'])
# def changeAccount():
#     req = request.json
#     #user.set_id(req["id"])
#     for key in users:
#         if key==req["id"]:
#             user=users[key]
#     user.set_name(req["name"])
#     user.set_lastname(req["lastname"])
#     user.set_address(req["address"])
#     user.set_city(req["city"])
#     user.set_country(req["country"])
#     user.set_phoneNumber(req["phoneNumber"])
#     user.set_email(req["email"])
#     user.set_password(req["password"])
#     for key in users:
#         if key==req["id"]:
#             users.pop(key)
#             break
#     users[req["id"]]=user
#     print(users[req["id"]])
#     return "Updated."
#
# @app.route("/accountVerification", methods=['POST'])
# def accountVerification():
#     req = request.json
#     if int(req["number"]) in creditCards:
#         if (creditCards[int(req["number"])]).get_csc() == int(req["csc"]) :
#             #provjeriti expirationDate sa danasnjim datumom (dd/yy)
#             if int(req["id"]) in users:
#                 users[int(req["id"])].set_verified(True)
#             else:
#                 return "Id for verification doesn't exists."
#             creditCards[int(req["number"])].withdraw(1)
#             users[req["id"]].set_onlineAccountBalance(0,"RSD")
#             print("Verified.")
#             return users[req["id"]].userToJSON()
#         else:
#             return "Invalid CSC."
#     else:
#         return "Verification failed."
#
# @app.route("/depositOnAccount", methods=['POST'])
# def depositOnAccount():
#     req = request.json
#     print(req["amount"])
#     print(req["rsdBalance"])
#     if int(req["id"]) in users:
#         user=users[int(req["id"])]
#     pom_creditCard=None
#     if user.get_creditCardNum()  in creditCards:
#         pom_creditCard=creditCards[user.get_creditCardNum()]
#     if((int(req["amount"]) + int(req["rsdBalance"]))  <= pom_creditCard.get_balance()):
#         users[user.get_id()].depositRSDOnAccount(int(req["amount"]))
#         print("Successfully deposited.")
#         return user.userToJSON()
#     else:
#         print("DEPOSIT FAILED.")
#         return "Deposition failed."
