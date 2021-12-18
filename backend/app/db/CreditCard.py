from backend.app.db.__init__ import db


# class CreditCard(db.Model):
#     number = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     expirationDate = db.Column(db.String(8), nullable=False)
#     csc = db.Column(db.Integer, nullable=False)
#     balance = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # def __init__(self, number, username, expirationDate, csc):
    #     self.number = number
    #     self.username = username
    #     self.expirationDate = expirationDate
    #     self.csc = csc
    #     self.balance = 70
    #
    # def get_number(self):
    #     return self.number
    #
    # def set_number(self, number):
    #     self.number = number
    #
    # def get_username(self):
    #     return self.username
    #
    # def set_username(self, username):
    #     self.username = username
    #
    # def get_expirationDate(self):
    #     return self.expirationDate
    #
    # def set_expirationDate(self, expirationDate):
    #     self.expirationDate = expirationDate
    #
    # def get_csc(self):
    #     return self.csc
    #
    # def set_csc(self, csc):
    #     self.csc = csc
    #
    # def get_balance(self):
    #     return self.balance
    #
    # def set_balance(self, balance):
    #     self.balance = balance
    #
    # def withdraw(self,amount):
    #     self.balance -= amount
    #
    # def deposit(self,amount):
    #     self.balance += amount
