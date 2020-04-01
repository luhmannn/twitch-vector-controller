from src.parser.responseparser import ResponseParser
from src.parser.messageparser import MessageParser
from src.parser.reconnectparser import ReconnectParser
from src.parser.pongparser import PongParser

class TypeToParser():

    def __init__(self):
        pass

    def get_parser(self, messageType):

        switcher = {
            "RESPONSE": ResponseParser(),
            "MESSAGE": MessageParser(),
            "RECONNECT": ReconnectParser(),
            "PONG": PongParser()
        }

        parserClass = switcher.get(messageType)
        return parserClass