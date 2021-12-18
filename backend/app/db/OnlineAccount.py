 #region
#
# from . import db
#
# class OnlineAccount(db.Model):
#     creditCardNum = db.Column(db.Integer)
#     balance = db.Column(db.Float)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#
#
#     def __init__(self, creditCardNum):
#         self.creditCardNum = creditCardNum
#         self.balances = {}
#
#     def get_creditCardNum(self):
#         return self.creditCardNum
#
#     def set_creditCardNum(self, creditCardNum):
#         self.creditCardNum = creditCardNum
#
#     def get_balances(self):
#         return self.balance
#
#     def set_balances(self, balance, key):
#         self.balances.update({key: balance})
#
#     def depositRSD(self, value):
#         if "RSD" in self.balances:
#             self.balances["RSD"] += value
#         else:
#             self.balnces["RSD"]=value
#
#     def __str__(self):
#          return "Creditcard number: "+self.creditCardNum+"\nBalances: "+ self.balances
#endregion