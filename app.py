import os
from src.twitchparser import TwitchParser
from src.chatbot import Chatbot
from src.actionresolver import ActionResolver

if __name__ == "__main__":
    # Get the oauth from .env not included in git
    twitch_oauth = os.getenv('TWITCH_OAUTH', 'You need to have a .env file with a variable TWITCH_OAUTH set to a value from https://twitchapps.com/tmi/')

    # instantiate dependencies
    parser = TwitchParser()
    actionResolver = ActionResolver()
    
    # Run the chatbot
    chatbot = Chatbot("irc.chat.twitch.tv", 6667, parser, twitch_oauth, "luhbert", "luhmannn", actionResolver)
