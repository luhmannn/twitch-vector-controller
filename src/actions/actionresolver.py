from src.vector.vector_say import VectorSay
from src.vector.vector_bananas import VectorBananas
from src.actions.sub import Subscription
import logging

class ActionResolver():

    def __init__(self):
        self.actions = {
            "sub": Subscription(),
            "resub": Subscription(),
            "Make Vector Speak": VectorSay(),
        }

    def get(self, command):
        logging.debug('attempt to get command: %s' % command)
        return self.actions.get(command)
