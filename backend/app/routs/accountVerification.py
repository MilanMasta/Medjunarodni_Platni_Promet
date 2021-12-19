



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