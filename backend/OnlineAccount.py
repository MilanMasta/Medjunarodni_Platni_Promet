class OnlineAccount:

    def __init__(self, creditCardNum):
        self.creditCardNum = creditCardNum
        self.balance = 0
        self.verified = False

    def get_creditCardNum(self):
      return self.creditCardNum

    def set_creditCardNum(self, creditCardNum):
      self.creditCardNum = creditCardNum

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_verified(self):
        return self.verified

    def set_verified(self, verified):
        self.verified = verified
