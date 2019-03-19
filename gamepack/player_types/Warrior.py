
from gamepack.player.Player import Player

class Warrior(Player):

    def __init__(self, name):
        Player.__init__(self, name)
        self.strength = 1

        # Default combat mvoes
        self.combat_moves = [
            'punch',
            'kick',
            'shove',
            'block'
        ]
    
    def get_combat_moves(self):
        return 'Combat moves: ' + ', '.join(self.combat_moves)
