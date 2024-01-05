class TomeOfKnowledge:
    def __init__(self):
        self._knowledge = 0  

    @property
    def knowledge(self):
        print("You feel the wisdom contained within the tome.")
        return self._knowledge

    @knowledge.setter
    def knowledge(self, value):
        print("The tome's knowledge expands.")
        if not isinstance(value, int) or value < 0:
            raise ValueError("Knowledge must be a non-negative integer.")
        self._knowledge = value

    @knowledge.deleter
    def knowledge(self):
        print("The tome's knowledge vanishes into the aether.")
        self._knowledge = 0

tome = TomeOfKnowledge()
tome.knowledge = 42  
print(tome.knowledge)  
del tome.knowledge  
print(tome.knowledge)