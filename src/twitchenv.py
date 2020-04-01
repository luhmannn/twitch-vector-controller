import os

class TwitchEnvironment():

    def __init__(self):
        self.twitch_irc_token = os.getenv('TWITCH_OAUTH', '')
        self.twitch_client_id = os.getenv('TWITCH_CLIENT_ID', '')
        self.twitch_client_secret = os.getenv('TWITCH_CLIENT_SECRET', '')
        self.twitch_code = os.getenv('TWITCH_CODE', 'Must set code in .env to get first Oauth-token')
        self.twitch_channels = os.getenv('TWITCH_CHANNELS', '')
        self.twitch_topics = os.getenv('TWITCH_TOPICS', '')
        self.twitch_nick = os.getenv('TWITCH_NICK', '')
        self.twitch_prefix = os.getenv('TWITCH_PREFIX', '')
        
    def get_twitch_client_id(self):
        return self.twitch_client_id

    def get_twitch_client_secret(self):
        return self.twitch_client_secret

    def get_twitch_code(self):
        return self.twitch_code
    
    def get_twitch_irc_token(self):
        return self.twitch_irc_token
    
    def get_twitch_channels(self):
        return self.twitch_channels
    
    def get_twitch_topics(self):
        return self.twitch_topics
    
    def get_twitch_nick(self):
        return self.twitch_nick
    
    def get_twitch_prefix(self):
        return self.twitch_prefix