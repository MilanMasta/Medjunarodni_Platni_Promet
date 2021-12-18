# from flask import request
# from .__init__ import app
# from .db.__init__ import sql_cursor
#
#
# @app.route("/register", methods=['POST'])
# def register():
#     print("Pocetak")
#     req = request.json
#     print(req)
#     query_num_of_useres = "SELECT max(id) FROM DataBaseDRS.user"
#     email = req["email"]
#     query_email_check = "SELECT Count(*) FROM DataBaseDRS.user WHERE email='{}'".format(
#         email)  # if 0 there is no such mail in DB
#
#     print("Sredina")
#
#     users_num = sql_cursor.execute(query_num_of_useres)
#     email_check = sql_cursor.execute(query_email_check)
#     query_add_user = 'INSERT INTO DataBaseDRS.user (user.id,user.name,user.lastname,user.address,user.city,' \
#                      'user.country,user.phoneNumber,user.email,user.password) values ({},"{}","{}","{}","RS",' \
#                      '0656662789,"mialn@gmail.com","sifra")'.format(
#         users_num + 1, req["name"], req["lastname"],
#         req["adress"], req["city"], req["country"], req["phoneNumber"], req["email"], req["password"])
#
#     if email_check == 0:
#         sql_cursor.execute(query_add_user)
#     else:
#         return "User with that email already exists"
#
# #
# # @app.route("/login", methods=['POST'])
# # def login():
# #     req = request.json
# #     for key in users:
# #         print("LOGIN")
# #         print(users[key])
# #         if users[key].get_email() == req["email"]:
# #             if (users[key].get_password() == req["password"]):
# #                 print(users[key].userToJSON())
# #                 return users[key].userToJSON()
# #             else:
# #                 return "Invalid password."
# #
# #     return "User doesn't exist."
# #
# #
# # @app.route("/changeAccount", methods=['POST'])
# # def changeAccount():
# #     req = request.json
# #     # user.set_id(req["id"])
# #     for key in users:
# #         if key == req["id"]:
# #             user = users[key]
# #     user.set_name(req["name"])
# #     user.set_lastname(req["lastname"])
# #     user.set_address(req["address"])
# #     user.set_city(req["city"])
# #     user.set_country(req["country"])
# #     user.set_phoneNumber(req["phoneNumber"])
# #     user.set_email(req["email"])
# #     user.set_password(req["password"])
# #     for key in users:
# #         if key == req["id"]:
# #             users.pop(key)
# #             break
# #     users[req["id"]] = user
# #     print(users[req["id"]])
# #     return "Updated."
# #
# #
# # @app.route("/accountVerification", methods=['POST'])
# # def accountVerification():
# #     req = request.json
# #     if int(req["number"]) in creditCards:
# #         if (creditCards[int(req["number"])]).get_csc() == int(req["csc"]):
# #             # provjeriti expirationDate sa danasnjim datumom (dd/yy)
# #             if int(req["id"]) in users:
# #                 users[int(req["id"])].set_verified(True)
# #             else:
# #                 return "Id for verification doesn't exists."
# #             creditCards[int(req["number"])].withdraw(1)
# #             users[req["id"]].set_onlineAccountBalance(0, "RSD")
# #             print("Verified.")
# #             return users[req["id"]].userToJSON()
# #         else:
# #             return "Invalid CSC."
# #     else:
# #         return "Verification failed."
# #
# #
# # @app.route("/depositOnAccount", methods=['POST'])
# # def depositOnAccount():
# #     req = request.json
# #     print(req["amount"])
# #     print(req["rsdBalance"])
# #     if int(req["id"]) in users:
# #         user = users[int(req["id"])]
# #     pom_creditCard = None
# #     if user.get_creditCardNum() in creditCards:
# #         pom_creditCard = creditCards[user.get_creditCardNum()]
# #     if ((int(req["amount"]) + int(req["rsdBalance"])) <= pom_creditCard.get_balance()):
# #         users[user.get_id()].depositRSDOnAccount(int(req["amount"]))
# #         print("Successfully deposited.")
# #         return user.userToJSON()
# #     else:
# #         print("DEPOSIT FAILED.")
# #         return "Deposition failed."
