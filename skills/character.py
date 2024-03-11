from abc import abstractmethod

class Character:
    """ a class defining all Characters """
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def fight(self, skill: str):
        """ Characters fight using skills """
        pass