
from gamepack.equipment.Equipment import Equipment
from gamepack.inventory.Inventory import Inventory

class Player(object):

    def __init__(self, name = ''):
        self.name = name
        self.health = 100
        self.equipment = Equipment()
        self.inventory = Inventory()
    
    def get_equipment_stats(self):
        return str(self.equipment)
    
    def __str__(self):
        return '%s [%i / 100]' % (self.name, self.health)