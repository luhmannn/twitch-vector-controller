from src.vector.vector_say import VectorSay
from src.vector.vector_bananas import VectorBananas

class ActionResolver():

    def __init__(self):
        self.actions = {
            "!say": VectorSay(),
            "!bananas": VectorBananas()
        }

    def get(self, command):
        return self.actions.get(command)


