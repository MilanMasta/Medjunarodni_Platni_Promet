from backend.app.db.User import User
from flask import request
from backend.app import app


@app.route("/login", methods=['GET', 'POST'])
def login():
    req = request.json
    try:
        user = User.query.filter_by(email='{}'.format(req["email"])).one()  # user ce biti taj user ako postoji
        User.query.filter_by(email='{}'.format(req["email"])).all()
        if(user.password == req["password"]):
            print(user.userToJSON())
            return user.userToJSON()
        else:
            return "Invalid password."
    except:
        return "User doesn't exist."
