
import uuid

class Item(object):

    def __init__(self, name = '', count = 0,  value = 0):
        self.id = uuid.uuid4()
        self.name = name
        self.count = count
        self.value = value
    
    def __eq__(self, other_item):
        return self.id == other.id
    
    def __str__(self):
        return '%s [count: %i, value: %i]' % (
            self.name,
            self.count,
            self.value,
        )