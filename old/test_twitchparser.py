import unittest
from src.parser.twitchparser import TwitchParser

class TestTwitchParser(unittest.TestCase):
 
    def test_ping_parse(self):    
        # arrange
        parser = TwitchParser.TwitchParser()

        # act
        contains_ping = parser.contains_ping('PING :tmi.twitch.tv\r\n')

        # assert
        self.assertTrue(contains_ping)
        
