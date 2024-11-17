class Attribute:
    name: str = ""
    next_level_exp = 32
    exp = 0
    level = 1

    def __init__(self, name):
        self.name = name

    def up_level():
        next_level_exp += 32 * (level / 2) + 6
        exp = 0
        level += 1
        
