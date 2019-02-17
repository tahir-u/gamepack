
class MoneyPouch(object):

    def __init__(self):
        self.amount = 0
    
    def deposit(self, amount):
        if amount <= 0:
            return self.amount
        self.amount += amount
        return self.amount
    
    def withdraw(self, amount):
        if amount <= 0 or amount > self.amount:
            return self.amount
        self.amount -= amount
        return self.amount
    
    def empty_pouch(self):
        self.amount = 0
        return self.amount
    
    def __str__(self):
        return 'Your money pouch currently contains %i coins' % (self.amount)