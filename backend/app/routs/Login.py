from backend.app.db.User import User
from flask import request
from backend.app import app


@app.route("/login", methods=['GET', 'POST'])
def login():
    req = request.json
    user = User.query.filter_by(email='{}'.format(req["email"])).one() # user ce biti taj user ako postoji
    if(User.query.filter_by(email='{}'.format(req["email"])).all()): #postoji email
        if(user.password == req["password"]):
            return user.userToJSON()
        else:
            return "Invalid password."
    else:
        return "User doesn't exist."