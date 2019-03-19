
from gamepack.player.Player import Player

class Warrior(Player):

    def __init__(self, name):
        Player.__init__(self, name)
        self.magic = 1

        # Default magic spells
        self.magic_spells = [
            'air wave',
            'weaken',
            'barrier'
        ]
    
    def get_magic_spells(self):
        return 'Magic spells: ' + ', '.join(self.magic_spells)
    