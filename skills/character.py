
class Character:
    """ a class defining all Characters """
    def __init__(self, name: str, level: int, skill_trees: [], action_skill: str,  skill_points: int):
        self.name = name
        self.level = level
        self.skill_trees = skill_trees
        self.action_skill = action_skill
        self.skill_points = skill_points

  