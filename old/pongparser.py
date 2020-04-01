from src.domain.reconnect import Reconnect
from src.domain.pong import Pong
import json 

class PongParser():

    def __init__(self):
        pass

    def parse(self, message):
        msg = json.loads(message)

        responseType = msg.get('type')

        response = Pong(responseType)
        return response