from src.vectorsay import VectorSay

class ActionResolver():

    def __init__(self):
        self.actions = {
            "!say": VectorSay()
        }

    def get(self, command):
        return self.actions.get(command)


