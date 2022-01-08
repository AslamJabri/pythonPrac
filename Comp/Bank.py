class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        
        self.balance = self.balance-amount

    def deposit(self, amount):
        # write code herss
        self.balance = amount+self.balance

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self,):
        #return the intrest rate 
        return  (self.balance * self.interestRate)/100
        


# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object
print(demo1.getBalance())
(demo1.deposit(2000))
(demo1.withdrawal(500))
print(demo1.getBalance())
print(demo1.interestAmount())