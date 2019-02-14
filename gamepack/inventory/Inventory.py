
class Inventory(object):

    def __init__(self, size = 20):
        self.size = 20
        self.contents = []
    
    def __str__(self):
        content = ['%s\n' % str(i) for i in self.contents].join('')
        
        return '''Inventory contents:
        %s
        ''' % (
            content
        )