from src.domain.reconnect import Reconnect
import json 

class ReconnectParser():

    def __init__(self):
        pass

    def parse(self, message):
        msg = json.loads(message)

        responseType = msg.get('type')

        response = Reconnect(responseType)
        return response