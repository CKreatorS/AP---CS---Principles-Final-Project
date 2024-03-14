
class Character:
    """ a class defining all Characters """
    def __init__(self, name: str, level: int, skill_trees: [], weapon: bool):
        self.name = name
        self.level = level
        self.skill_trees = skill_trees
        self.weapon = weapon

    def fight(self) -> str:
        return self.name + " is at level " + self.level + " and fights with the skill trees" + self.skill_trees
    
class Type(Character): 
    """ A class that identifies types of playable characters """
    def __init__(self, name: str, level: int, skill_trees: [], weapon: str, has_weapon: bool):
        