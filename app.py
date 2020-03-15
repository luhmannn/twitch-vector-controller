import os
from Vector import Vector
from TwitchParser import TwitchParser
from Chatbot import Chatbot

if __name__ == "__main__":
    twitch_oauth = os.getenv('TWITCH_OAUTH', 'You need to have a .env file with a variable TWITCH_OAUTH set to a value from https://twitchapps.com/tmi/')

    parser = TwitchParser()
    vector = Vector()
    chatbot = Chatbot(parser, vector, twitch_oauth)
