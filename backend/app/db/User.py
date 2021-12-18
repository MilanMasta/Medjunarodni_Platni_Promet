# from .CreditCard import CreditCard
# from . import db
# import json
# import copy
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#     lastname = db.Column(db.String(20), nullable=False)
#     # address = db.Column(db.String(20), nullable=False)
#     # city = db.Column(db.String(20), nullable=False)
#     # country = db.Column(db.String(20), nullable=False)
#     # phoneNumber = db.Column(db.String(15), nullable=False)
#     # email = db.Column(db.String(20), nullable=False)
#     # password = db.Column(db.String(20), nullable=False)
#     # verified = db.Column(db.Boolean, default=False)
#     # creditCards = db.relationship('CreditCard', backref='id', lazy=True)
#
#     def __repr__(self):
#         return f"User('{self.id}', '{self.name}', '{self.creditCardNum}')"
#
#     def __init__(self, id, name, lastname, address, city, country, phoneNumber, email, password, creditCardNum):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.address = address
#         self.city = city
#         self.country = country
#         self.phoneNumber = phoneNumber
#         self.email = email
#         self.password = password
#         self.verified = False
#         self.onlineAccount = OnlineAccount(-1)
#         self.creditCardNum = creditCardNum
#
#     def get_id(self):
#         return self.id
#
#     def set_id(self, id):
#         self.id = id
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_lastname(self):
#         return self.lastname
#
#     def set_lastname(self, lastname):
#         self.lastname = lastname
#
#     def get_address(self):
#         return self.address
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_city(self):
#         return self.city
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_country(self):
#         return self.country
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_phoneNumber(self):
#         return self.phoneNumber
#
#     def set_phoneNumber(self, phoneNumber):
#         self.phoneNumber = phoneNumber
#
#     def get_email(self):
#         return self.email
#
#     def set_email(self, email):
#         self.email = email
#
#     def get_password(self):
#         return self.password
#
#     def set_password(self, password):
#         self.password = password
#
#     def get_verified(self):
#         return self.verified
#
#     def set_verified(self, verified):
#         self.verified = verified
#
#     def get_onlineRacun(self):
#         return self.onlineRacun
#
#     def set_onlineAccountBalance(self, balance, key):
#         self.onlineAccount.set_balances(balance, key)
#
#     def get_creditCardNum(self):
#         return self.creditCardNum
#
#     def set_creditCardNum(self, creditCardNum):
#         self.creditCardNum = creditCardNum
#
#     def depositRSDOnAccount(self, value):
#         self.onlineAccount.depositRSD(value)
#
#     def __str__(self):
#         return f"ID : {self.id}\nName : {self.name}\nLastname : {self.lastname}\nAddress : {self.address}\nCity: {self.city}\nCountry : {self.country}\n" \
#                f"Phone number : {self.phoneNumber}\nEmail : {self.email}\nPassword : {self.password}."
#
#     def userToJSON(self):
#         pom = copy.deepcopy(self)
#         pom.onlineAccount = pom.onlineAccount.__dict__
#         return json.dumps(pom.__dict__)
