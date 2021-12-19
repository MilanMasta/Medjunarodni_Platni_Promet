


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
