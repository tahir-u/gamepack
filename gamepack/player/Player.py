
from gamepack.equipment.Equipment import Equipment
from gamepack.inventory.Inventory import Inventory
from gamepack.moneypouch.MoneyPouch import MoneyPouch

class Player(object):

    def __init__(self, name = ''):
        self.name = name
        self.health = 100
        self.equipment = Equipment()
        self.inventory = Inventory()
        self.moneypouch = MoneyPouch()
    
    def get_equipment_stats(self):
        return str(self.equipment)
    
    def get_inventory(self):
        return str(self.inventory)
    
    def check_moneypouch(self):
        return str(self.moneypouch)
    
    def __str__(self):
        return '%s [%i / 100]' % (self.name, self.health)