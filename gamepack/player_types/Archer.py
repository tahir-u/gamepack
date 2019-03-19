
from gamepack.player.Player import Player

class ArcherPlayer):

    def __init__(self, name):
        Player.__init__(self, name)
        self.range = 1

        # Default range moves
        self.range_moves = [
            'quick shot',
            'double shot',
            'dash'
        ]
    
    def get_range_moves(self):
        return 'Range moves: ' + ', '.join(self.range_moves)
