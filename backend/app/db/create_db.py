# # # import mysql.connector
# import json
# import datetime
# from backend.app.db.Balances import Balances
# import copy
#
# from backend.app.db.CCards import CCards
# from backend.app.db.CreditCard import CreditCard
from backend.app.db import db
from backend.app.db.CCards import CCards
from backend.app.db.Transaction import Transaction
from backend.app.Encoder import AlchemyEncoder
# from backend.app.db.User import User
# from backend.app.db import db
# #
# # connection = mysql.connector.connect(
# #     user='root',
# #     password='sifra',
# #     host='localhost',
# #     )
# # my_cursor = connection.cursor()
# #
# # #kreiranje baze
# # my_cursor.execute("CREATE DATABASE DataBaseDRS")
# #
# #
# # my_cursor.close()
# # connection.close()
#
# # user1 = User.query.filter_by(email='a').one()
# # user1.userToJSON()
# # pom = copy.deepcopy(self)
# # pom.onlineAccount = pom.onlineAccount.__dict__
# # print(json.dumps(pom.__dict__))
#
# # print(User.query.all())
# user = User(name="aa", lastname="aa", address="aa", city="aa",
#             country="aa", phoneNumber=432, email="aa", password="aa",
#             verified=False)
# print(user.userToJSON())

# # db.session.add(user)
# # db.session.commit()
#
# for i in range(0, 10):
#     cCards = CCards(number=str(1000000000000000+i), expirationDate="11/22", csc=100+i,balance=1100+i*1540)
#     db.session.add(cCards)
#     db.session.commit()

# balance = Balances(balance=0, valute="AUD",user_id=1)
#
# print("fdsfds")
# db.session.add(balance)
# db.session.commit()
# from backend.app.db import db
#
# tra = Transaction(state="U obradi", sender="a" , reciever="1000000000000007",amount=2000,destination="Banka")
# db.session.add(tra)
# db.session.commit()
# from backend.app.db.Balances import Balances
# senderBalance = Balances.query.filter_by(user_id='{}'.format(1), valute='RSD').one()
# print(senderBalance.user_id)
# balances = Balances.query.filter_by(user_id='7').all()
# for b in balances:
#     print(b.valute)

# balances = Balances.query.filter_by(user_id='{}'.format(7)).all()
# data = []
# for b in balances:
#     data.append("{}: {}".format(b.valute, b.balance))
# print(data)
# print(json.dumps(data))

# cCard =CCards.query.filter_by(number='1000000000000001',csc='{}'.format(101)).one() #NUMBER DOESN'T EXIST
# y = str(cCard.expirationDate).split("/")
# m = int(y[0])
# y1 = int("20" + y[1])
# print(datetime.date.today().year)
# print(datetime.date.today().month)
# if (datetime.date.today().year < y1):
# elif(datetime.date.today().year == y1):
#     if(datetime.date.today().month < m ):
#         print("Sve dobro")

# kar = CreditCard(number="fdsfsdfs", csc=322, balance=413213, user_id=1,
#                  expirationDate="dfsfs")
# db.session.add(kar)
# db.session.commit()
#
# kar = CreditCard.filter_by(user_id='{}'.format(1)).all()
# print(kar)
# user = User.filter_by(id='{}'.format(1)).one()
# rsdBalanceUser = Balances.filter_by(user_id='{}'.format(1), valute="RSD").one()
#
# user = User.query.filter_by(id='{}'.format(2)).one()
# user.verified = False
# db.session.commit()

# transactions = Transaction.query.filter_by(senderId='{}'.format(1)).all()
# data = []
# for t in transactions:
#     print(t)
#     data.append(t.__dict__)
#
# # print(data)
# c = Transaction.query.filter_by(sender='{}'.format(1)).all()
# print(json.dumps(c, cls=AlchemyEncoder))


# data = []
# json_strng = json.dumps([t.__dict__ for t in transactions])
# # for t in transactions:
#
#     print(t.__dict__)
#     data.append("id" + f"{t.id}")
#     # data.append(){ t }
#return("transactions": data)
# print(json_strng)

#transaction = Transaction.query.filter_by(id='{}'.format("6")).one()
