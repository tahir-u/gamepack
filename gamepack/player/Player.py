
class Player(object):

    def __init__(self, name = ''):
        self.name = name
        self.health = 100
    
    def __str__(self):
        return '%s [%i / 100]' % (self.name, self.health)