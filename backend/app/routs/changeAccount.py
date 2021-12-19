


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