from src.domain.response import Response
import json 

class ResponseParser():

    def __init__(self):
        pass

    def parse(self, message):
        msg = json.loads(message)

        responseType = msg.get('type')
        error = msg.get('error')
        nonce = msg.get('nonce')
        

        response = Response(responseType, error, nonce)
        return response