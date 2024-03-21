
class Character:
    """ a class defining all Characters """
    def __init__(self, name: str, level: int, skill_trees: [], weapon: bool):
        self.name = name
        self.level = level
        self.skill_trees = skill_trees
        self.weapon = weapon

    def fight(self) -> str:
        return self.name + " is at level " + self.level + " and fights with the skill trees" + str(self.skill_trees)
    
class Features(Character): 
    """ A class that identifies the features of playable characters """
    def __init__(self, name: str, level: int, skill_trees: [], action_skill: str, has_action_skill: bool):
        super().__init__(name, level, skill_trees, True)
        self.action_skill = action_skill 
        self.has_action_skill = has_action_skill

        self.has_action_skill = True
        
    def trees(self) -> str:
        return 'The character ' + self.name + ' has the action skill ' + self.action_skill
    
class Skill(Features):
    """ A class that identifies the action skill """
    def __init__(self, name: str, level: int, skill_trees: [], action_skill: str, has_action_skill: bool):
        super().__init__(name, level, skill_trees, action_skill, True)
        self.has_action_skill = has_action_skill
        self.has_action_skill = True

    def points(self) -> str:
        return 'it is ' + str(self.has_action_skill) + ' that ' + self.name + ' has an action skill'