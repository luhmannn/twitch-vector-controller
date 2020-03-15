from Vector import Vector
from TwitchParser import TwitchParser
from Vectorbot import Vectorbot

if __name__ == "__main__":
    parser = TwitchParser()
    vectorbot = Vectorbot()
    vector = Vector(parser, vectorbot)
