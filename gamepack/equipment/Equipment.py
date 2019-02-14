
class Equipment(object):

    def __init__(self):
        self.equipment = {
            'head': None,
            'neck': None,
            'chest': None,
            'legs': None,
            'feet': None,
            'shield': None,
            'weapon': None
        }
        self.bonuses = {
            'offensive': 0,
            'defensive': 0
        }
    
    def __str__(self):
        return '''
        Current Equipment:

        Head: %s,
        Neck: %s,
        Chest: %s,
        Legs: %s,
        Feet: %s,
        Shield: %s,
        Weapon: %s

        Current Bonuses (Offensive/Defensive):
        [%i / %i]
        ''' % (
            self.equipment.get('head'),
            self.equipment.get('neck'),
            self.equipment.get('chest'),
            self.equipment.get('legs'),
            self.equipment.get('feet'),
            self.equipment.get('shield'),
            self.equipment.get('weapon'),
            self.bonuses.get('offensive'),
            self.bonuses.get('defensive')
        )