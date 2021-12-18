from flask import Flask

app = Flask(__name__)



from flask import request
# from backend.app import app
from backend.app.db import sql_cursor

# user = '{"id": "0", "name": "", "lastname": "", "address": "", "city": "", "country": "", "phoneNumber": "", "email": "", "password": ""}'
# x = []
# users = {}  # dict -> key = id && value = user
# creditCards = {}  # dict -> key = creditCardNum && value = creditCard
# global usersCount
# usersCount = 0


@app.route("/register", methods=['GET'])
def register():
    print("Pocetak")
    # req = request.json
    # print(req)
    # query_num_of_useres = "SELECT max(id) FROM DataBaseDRS.user"
    # email = req["email"]
    # query_email_check = "SELECT Count(*) FROM DataBaseDRS.user WHERE email='{}'".format(
    #     email)  # if 0 there is no such mail in DB
    #
    # print("Sredina")
    #
    # users_num = sql_cursor.execute(query_num_of_useres)
    # email_check = sql_cursor.execute(query_email_check)
    # query_add_user = 'INSERT INTO DataBaseDRS.user (user.id,user.name,user.lastname,user.address,user.city,' \
    #                  'user.country,user.phoneNumber,user.email,user.password) values ({},"{}","{}","{}","RS",' \
    #                  '0656662789,"mialn@gmail.com","sifra")'.format(
    #     users_num + 1, req["name"], req["lastname"],
    #     req["adress"], req["city"], req["country"], req["phoneNumber"], req["email"], req["password"])
    #
    # if email_check == 0:
    #     sql_cursor.execute(query_add_user)
    #     return "Successfully registered."
    # else:
    return "User with that email already exists"


@app.route("/login", methods=['POST'])
def login():
    # req = request.json
    # for key in users:
    #     print("LOGIN")
    #     print(users[key])
    #     if users[key].get_email() == req["email"]:
    #         if (users[key].get_password() == req["password"]):
    #             print(users[key].userToJSON())
    #             return users[key].userToJSON()
    #         else:
    #             return "Invalid password."

    return "User doesn't exist."
