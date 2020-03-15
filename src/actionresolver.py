from src.vector.vector_say import VectorSay
from src.vector.vector_banana_eyes import VectorBananaEyes

class ActionResolver():

    def __init__(self):
        self.actions = {
            "!say": VectorSay()
        }

    def get(self, command):
        return self.actions.get(command)


