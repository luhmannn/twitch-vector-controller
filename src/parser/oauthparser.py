from src.domain.oauthset import OAuthSet
import json

class OauthParser():

    def __init__(self):
        pass

    def parse_new_oauth_response(self, message):
        authtoken = json.loads(message.content)
        return OAuthSet(authtoken['access_token'], authtoken['refresh_token'])