
from gamepack.item.Item import Item

class StackableItem(Item):

    def __init__(self, name = '', value = 0, count = 0):
        Item.__init__(self, name, value, count)
        self.stackable = True
    
    def add_to_stack(self, item):
        if item.name == self.name:
            self.count += item.count
            self.value = (item.count * self.value)
    
    def remove_from_stack(self, count):
        if count > 0 and count >= self.count:
            self.count -= count
            self.value = (self.value - (count * self.value))
    
    def __str__(self):
        return super.__str__(self)