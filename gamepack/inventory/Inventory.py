
class Inventory(object):

    def __init__(self, size = 20):
        self.size = 20
        self.contents = []
    
    def add(self, item):
        if self.size == 20:
            return self.contents
        self.contents.append(item)
        self.size += 1

        return self.contents
    
    def remove(self, item):
        # TODO: implement alongside Item class, for comparing items
        pass
    
    def contains(self, item):
        # TODO: implement alongside Item class, for comparing items
        pass
    
    def __str__(self):
        content = ['%s\n' % str(i) for i in self.contents].join('')
        
        return '''Inventory contents:
        %s
        ''' % (
            content
        )