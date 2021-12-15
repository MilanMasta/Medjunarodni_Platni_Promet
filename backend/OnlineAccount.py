class OnlineAccount:

    def __init__(self, creditCardNum):
        self.creditCardNum = creditCardNum
        self.balance = 0

    def get_creditCardNum(self):
      return self.creditCardNum

    def set_creditCardNum(self, creditCardNum):
      self.creditCardNum = creditCardNum

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance += balance