from src.actions.reconnect import Reconnect
from src.actions.responsebadauth import ResponseBadAuth 
from src.actions.registerpong import RegisterPong

class ActionResolver():

    def __init__(self, oauth):
        self.oauth = oauth
        self.actions = {
            "ERRORERR_BADAUTH": ResponseBadAuth(oauth),
            "RECONNECT": Reconnect(oauth),
            "PONG": RegisterPong()
        }

    def get(self, messagetype, response):
        if (hasattr(response, 'error')):
            return self.actions.get("%s%s" % (messagetype, response.error or ''))
        else:
            return self.actions.get("%s" % (messagetype))





