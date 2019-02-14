
import uuid

class Item(object):

    def __init__(self, name = '', value = 0):
        self.id = uuid.uuid4()
        self.name = name
        self.value = value
        self.count = 1
    
    def __eq__(self, other_item):
        return self.id == other.id
    
    def __str__(self):
        return '%s [value: %i, count: %i]' % (
            self.name,
            self.value,
            self.count
        )